# This script was created by cx_Freeze with the following command: cxfreeze-quickstart
# cx_Freeze is a tool that turns python scripts into standalone executable binaries.
# Project page: https://pypi.org/project/cx-Freeze/
# Project documentation: https://cx-freeze.readthedocs.io/en/latest/
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'build_exe': 'build/sas-ds-generator-script', 
    'packages': [], 
    'excludes': [], 
    'include_files': ['env_config.yaml']
}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name='sas-ds-generator-script')
]

setup(name='sas-ds-generator-script',
      version = '1.0',
      description = 'sas-ds-generator-script',
      options = {'build_exe': build_options},
      executables = executables)

#Create input_files directory in final build
script_path = os.path.abspath(__file__)
os.mkdir(os.path.dirname(script_path) + '/build/sas-ds-generator-script/input_files')