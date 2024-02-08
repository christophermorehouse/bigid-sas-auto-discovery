import os
from datetime import datetime
from modules import ds_import, create_access_token, update_scope

# Record the start time
start_time = datetime.now()
print(f"Process start time: {start_time}")

# Set parent directory
script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)

# Get SAS path input files
sas_path_files = []
try:
    # Run this if executing from cx_Freeze binary
    input_path = dir_path + '/../input_files/'
    for name in os.listdir(input_path):
        sas_path_files.append(name)
except:
    #Run this if executing from python interpreter
    input_path = dir_path + '/input_files/'
    for name in os.listdir(input_path):
        sas_path_files.append(name)

print('List of SAS path files found in ' + input_path + ':')
print(sas_path_files)

# Generate an access token to be used for the ds_connections and scope APIs
bigid_auth_token = create_access_token.get_access_token()

#Get scope_id and description of supplied scope name along with a list of data sources under scope_id
scope_id, scope_description, scope_ds_list = update_scope.get_scope_id(bigid_auth_token)

# Create individual DS connections from SAS path input files and import into BigID.
final_ds_names_list = []
for file in sas_path_files:
    ds_names_list = ds_import.init_import(bigid_auth_token, file, input_path)
    # Create a final list of all DS names from all SAS path input files
    final_ds_names_list.extend(ds_names_list)

#Update the scope with the full list of data sources imported
final_ds_names_list.extend(scope_ds_list)
update_scope.update_scope(scope_id, scope_description, bigid_auth_token, final_ds_names_list)
        
# Record the end time and calculate total runtime
end_time = datetime.now()
total_run_time = end_time - start_time
print(f"Process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Process finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Total run time: {total_run_time}")
input("Press Enter to exit...")