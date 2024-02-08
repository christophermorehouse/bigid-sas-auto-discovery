import requests, urllib3
from modules import config

def get_access_token():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': config.refresh_token
    }

    try:
        system_token = requests.request("GET", config.bigid_url + '/api/v1/refresh-access-token', headers=headers).json()['systemToken']
    except:
        # Suppress non https warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        system_token = requests.request("GET", config.bigid_url + '/api/v1/refresh-access-token', headers=headers, verify=False).json()['systemToken']

    return system_token