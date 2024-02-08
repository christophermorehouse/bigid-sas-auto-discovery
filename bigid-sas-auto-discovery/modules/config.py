import os, yaml

# Set parent directory
path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.dirname(path))

# Get configuration from yaml file
try:
    # Run this if executing from cx_Freeze binary
    with open(dir_path + '/../env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)
except:
    #Run this if executing from python interpreter
    with open(dir_path + '/env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)

print('env_config.yaml found in: ' + dir_path + '/')

# Set global variables with values from yaml file
resource_address = config_yaml['Script Parameters'][0]['resource_address']
scope_name = config_yaml['Script Parameters'][1]['scope_name']
ds_name_prefix = config_yaml['Script Parameters'][2]['ds_name_prefix']
max_threads = config_yaml['Script Parameters'][3]['max_threads']

bigid_url = config_yaml['BigID Server'][0]['bigid_url']
refresh_token = config_yaml['BigID Server'][1]['bigid_auth_token']