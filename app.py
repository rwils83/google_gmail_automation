from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#If modifying scopes change this
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CRED_FILE =
def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                 CRED_FILE, SCOPES)
            creds = flow.run_local_server()
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


    service = build('gmail', 'v1', credentials = creds)

    
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No Labels Found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


if __name__ == '__main__':
    main()
