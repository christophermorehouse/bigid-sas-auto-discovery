import json, requests, urllib3
from modules import config

def get_scope_id(bigid_auth_token):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': bigid_auth_token
    }

    try:
        response = requests.request("GET", config.bigid_url + '/api/v1/access-management/scopes', headers=headers).json()['data']
    except:
        # Suppress non https warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("GET", config.bigid_url + '/api/v1/access-management/scopes', headers=headers, verify=False).json()['data']

    target_scope_name = config.scope_name
    # Parse the response json and grab the id, description, and existing DS list of the specified scope name
    for scope in response['scopes']:
        if scope['name'] == target_scope_name:
            scope_id = scope['id']
            scope_description = scope['description']
            scope_ds_list = scope['dataSourceNames']

    return scope_id, scope_description, scope_ds_list

def update_scope(scope_id, scope_description, bigid_auth_token, final_ds_names_list):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bigid_auth_token
    }

    payload = json.dumps({
        "description": scope_description,
        "dataSourceNames": final_ds_names_list
    })

    try:
        response = requests.request("PUT", config.bigid_url + '/api/v1/scopes/' + scope_id, headers=headers, data=payload)
        print('Update scope response:')
        print(response)
    except:
        # Suppress non https warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("PUT", config.bigid_url + '/api/v1/scopes/' + scope_id, headers=headers, data=payload, verify=False)
        print('Update scope response:')
        print(response)