import requests
import json
import re
import os

class CreateConnection():

    def __init__(self, base_url, userName, password, ssl_verify=True, timeout=100):
        self.base_url = base_url
        self.userName = userName
        self.password = password
        self.ssl_verify = ssl_verify
        self.timeout = timeout

    def make_request(self, uri, method, body=None):
        headers = {
            "Accept": "application/json"
        }

        if body:
            body = json.dumps(body)

        response = requests.request(
            url = self.base_url + uri,
            method = method,
            auth=(self.userName, self.password),
            headers=headers,
            data=body,
            verify=self.ssl_verify,
            timeout=self.timeout
        )

        if response.status_code >= 300:
            raise Exception(f"{response.status_code}: {response.text}")

        response_data = response.json()
        assert 'result' in response_data

        return response_data['result']

    
    def get_user(self, email, sysparm_fields='name, sys_id, email'):
        uri = f'/api/now/table/sys_user?sysparm_query=email={email}&sysparm_fields={sysparm_fields}'
        method = 'GET'

        return self.make_request(uri, method)
    
