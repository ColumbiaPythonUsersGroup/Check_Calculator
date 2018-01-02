import requests
import json


def get_data():
    url = 'https://taxee.io/api/v2/federal/2017'
    token_value = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjVhMzg3MTRkZjNiYmEyNjgyZmY4N2FjNyIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTUxMzgyOTY3OX0.nfdDFdV3p4CDK-A3o_ZP4kXsInlh87YVCRTs-856vrg'
    header_value = {'Authorization': 'Bearer ' + token_value}
    try:
        response = requests.get(url, headers=header_value)

        print(response.status_code)
        print(response.text)
        print(response.json())
        json_data = json.loads(response)
        for key in json_data:
            var = key + " : " + json_data[key]
            print(var)
    except Exception as ce:
        print(ce)
