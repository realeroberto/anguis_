#!/usr/bin/env python

# anguis - A generic key-store library

# The MIT License (MIT)
# 
# Copyright (c) 2018-21 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# based on https://github.com/googleworkspace/python-samples/blob/master/drive/quickstart/quickstart.py

import os.path
import tempfile
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from anguis.base import AnguisBase

class AnguisGdrive(AnguisBase):

    def __init__(self, *args, **kwargs):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/drive']

        creds = None
        home = os.path.expanduser("~")
        tokenfile = os.path.join(home, 'token.json')
        credsfile = os.path.join(home, 'credentials.json')
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(tokenfile):
            creds = Credentials.from_authorized_user_file(tokenfile, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credsfile, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(tokenfile, 'w') as token:
                token.write(creds.to_json())

        self.service = build('drive', 'v3', credentials=creds)

        super(AnguisGdrive, self).__init__()

    def __del__(self):
        super(AnguisGdrive, self).__del__()

    def __getitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        file_metadata = {'name': key}
        with tempfile.NamedTemporaryFile() as fp:
            pickle.dump(value, fp)
            media = MediaFileUpload(fp.name, mimetype='octet/stream')
            file = self.service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()

    def __delitem__(self, key):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def keys(self):
        results = self.service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        return items

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
