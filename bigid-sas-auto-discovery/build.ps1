# Build executable
python setup.py build

# Remove cf_Freeze license
Remove-Item -Path ./build/sas-ds-generator-script/frozen_application_license.txt

# Create application zip for deployment
Set-Location ./build
Compress-Archive -Path ./sas-ds-generator-script -DestinationPath ./sas-ds-generator-script.zip