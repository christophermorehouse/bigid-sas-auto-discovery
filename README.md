# SAS Auto Discovery

## Author
Christopher Morehouse

## Description

The SAS Auto Discovery script retrieves a list of libraries from a SAS server and automatically creates a data source connection in BigID for every SAS library found. 

## Script Configuration

Before running the script, you will need to generate a refresh token. Refresh tokens are obtained from the BigID UI under Administration -> Access Management.
You will need to create the refresh token under a user who has the proper roles configured for making API calls.
Refer to the BigID documentation for specifics on users and roles.

Once you have the refresh token, edit the env_config.yaml with the proper environment settings:

```yaml

Script Parameters:
- resource_address: "Hostname of IP of SAS Server"
- scope_name: "BigID scope name the data source will belong to"
- ds_name_prefix: "Prefix to be added to Data Source name"
- max_threads: "number of threads the utility will run. this is 5 by default"

BigID Server:
- bigid_url: "URL of BigID server. example - https://bigidhost.com"
- bigid_auth_token: "Refresh token generated under BigID UI: Administration -> Access Management -> User"
```

Save the changes to the yaml config file and execute the script.

## Running the script

To execute the script using a python interpreter, you will first need to import the dependencies in the requirements.txt.
You can do this by running the following command: 

```sh
pip install -r requirements.txt
```

Once dependencies are installed, run the script with the following command: 

```sh
python main.py
```

## Build an executable binary for deployment

The preferred method for deployment is to build a self-contained package that includes all the dependencies as well as a run-time environment.
Using this method, users will not have to install python or any dependency libraries. They just edit the env_config.yaml and execute the binary.

cx_Freeze is used to build the binary and will need to be installed first in order to create the deployment package. For more information on cx_Freeze:

Project page: https://pypi.org/project/cx-Freeze/

Project documentation: https://cx-freeze.readthedocs.io/en/latest/

You can install cx_Freeze in a Python environment by running the following command:

```sh
pip install --upgrade cx_Freeze
```

Once cx_Freeze is installed you can continue with building the self-contained package by executing the build.sh script with the following command: 

```sh
./build.ps1
```

A "build" folder will get created that contains the directory with the executable and dependancy library. A zip of the executable directory also gets created.
You can send this zip to users or wherever the script will be deployed to.

To run the utility, just execute the sas-ds-generator-script.exe file
