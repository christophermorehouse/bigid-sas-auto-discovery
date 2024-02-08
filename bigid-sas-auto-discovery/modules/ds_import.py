import json, requests, urllib3
import concurrent.futures
from modules import config

def init_import(bigid_auth_token, file, input_path):

    # Read folder paths from a text file
    input_file_path = input_path + file
    with open(input_file_path, 'r') as file:
        folder_paths = [line.strip() for line in file]

    # Create list of DS names
    ds_names_list = []

    # Run multithreaded with the configured thread count to reduce runtime
    with concurrent.futures.ThreadPoolExecutor(config.max_threads) as executor:
        # Iterate through the folder paths
        for folder_path in folder_paths:
            # Check for a leading forward slash in path name. 
            # Then replace illegal characters in the path names with an underscore.
            if folder_path[0] == '/':
                ds_name = config.ds_name_prefix + folder_path.replace('/', '_').replace('.', '_')
            else:
                ds_name = config.ds_name_prefix + '_' + folder_path.replace('/', '_').replace('.', '_')
            ds_names_list.append(ds_name)
            # Create a DS import json and import into BigID
            executor.submit(ds_import_to_bigid, bigid_auth_token, ds_name, folder_path)
        
    return ds_names_list

def ds_import_to_bigid(bigid_auth_token, ds_name, folder_path):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': bigid_auth_token
    }

    # Create a dictionary for the JSON data
    ds_connection = {
        "ds_connection": {
            "name": f"{ds_name}",
            "enabled": "yes",
            "friendly_name": f"{ds_name}",
            "tags": [],
            "type": "sas",
            "resourceProperties": {
                "resourceAddress": f"{config.resource_address}",
                "resourceEntry": f"saslib '{folder_path}'"
            },
            "authStrategy": "bigIDCredentialAuthentication",
            "authenticationProperties": {
                "@authenticationType": "bigIDCredentialAuthentication",
                "username": "zmbigid1",
                "credentialID": [
                    {
                        "id": "MEXICO_SAS_CD",
                        "value": "MEXICO_SAS_CD",
                        "label": "MEXICO_SAS_CD"
                    }
                ]
            },
            "is_idsor_supported": True,
            "containerizedFilterType": "containerizedSpecificNameFilter",
            "containerizedFilter": {
                "@containerizedFilterType": "containerizedSpecificNameFilter",
                "specificNameFilters": {
                    "containerUseCase": {
                        "useCase": "INCLUDE",
                        "name": "SASLIB"
                    },
                    "objectNameUseCase": {
                        "useCase": "INCLUDE",
                        "name": ""
                    }
                }
            },
            "stopOnEnumerationFailure": False,
            "scanner_group": "MX-Scanner",
            "custom_fields": [],
            "owners_v2": [],
            "security_tier": "1",
            "location": "Mexico",
            "contentSamplingDropDown": "sampleLimit",
            "contentSamplingProperties": {
                "@contentSamplingType": "sampleLimit",
                "limit": 10000
            },
            "numberOfParsingThreads": "10",
            "classification_is_enabled": True,
            "ner_classification_is_enabled": False,
            "scanWindowName": [],
            "notAddToScope": True,
            "customFields": [],
            "differentialType": "differentialLastScanFilter",
            "differentialFilter": {"@differentialType": "differentialLastScanFilter"}
        }
    }

    ds_connections_json = json.dumps(ds_connection, indent=4)

    try:
        # Import DS connection to BigID
        response = requests.request("POST", config.bigid_url + '/api/v1/ds_connections', headers=headers, data=ds_connections_json)
        print(response.text + ' :has been created')
    except:
        # Suppress non https warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # Import DS connection to BigID
        response = requests.request("POST", config.bigid_url + '/api/v1/ds_connections', headers=headers, data=ds_connections_json, verify=False)
        print(response.text + ' :has been created')