#!/usr/bin/env python

import yaql
import yaml
import uuid
from anguis.fs import AnguisFS
from anguis.s3 import AnguisS3

dct = yaml.safe_load('''
customers_city:
  - city: New York
    customer_id: 1
  - city: Saint Louis
    customer_id: 2
  - city: Mountain View
    customer_id: 3
customers:
  - customer_id: 1
    name: John
    orders:
      - order_id: 1
        item: Guitar
        quantity: 1
  - customer_id: 2
    name: Paul
    orders:
      - order_id: 2
        item: Banjo
        quantity: 2
      - order_id: 3
        item: Piano
        quantity: 1
  - customer_id: 3
    name: Diana
    orders:
      - order_id: 4
        item: Drums
        quantity: 1
''')

cache = {'fs' : AnguisFS(), 's3' : AnguisS3(str(uuid.uuid4()), create=True)}
cache['fs']['customers_city'] = dct['customers_city']
cache['s3']['customers'] = dct['customers']

engine = yaql.factory.YaqlFactory().create()

expression = engine(
    '$.s3.customers.orders.selectMany($.where($.order_id = 4))')

print(expression.evaluate(data=cache))
