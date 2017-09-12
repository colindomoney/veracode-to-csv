![travis-ci build status](https://travis-ci.org/ctcampbell/veracode-to-csv.svg?branch=master)

This is not an official Veracode project. The Veracode support team will not be able to assist with troubleshooting. Please raise an issue on this project for improvements or bug fixes.

# Install

Download latest release from [releases/latest](https://github.com/ctcampbell/veracode-to-csv/releases/latest)

Requires Python 2.7

Install Veracode module veracode-api-signing (speak to your Veracode Solution Architect for this file)

    pip install veracode_api_signing-16.12.4-py2-none-any.whl

API credentials must be enabled on a Veracode account and placed in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

File permissions should be set appropriately

    chmod 600 ~/.veracode/credentials

Install other dependencies

    pip install -r requirements.txt

# Configure

Configuration is done in config.py

    # Logging
    debug_logging = True
    
    # Directory to output .csv files
    output_directory = "output"
    
    # UTF-8 encoded file containing list of applications to include.
    # Note - an empty file will include all application profiles
    app_include_list = "app_include_list.txt"
    
    # Include static/dynamic flaws
    include_static_flaws = True
    include_dynamic_flaws = True
    
    # Include sandboxes
    include_sandboxes = True
    
    # Add headers to csv files
    include_csv_headers = True
   
    # Proxy configuration, see http://docs.python-requests.org/en/master/user/advanced/#proxies for options
    proxies = {"https": "http://user:pass@10.10.10.10:8080/"}

# Run

    python veracodetocsv.py
    
A text file `processed_builds.txt` keeps track of which builds have been successfully processed.

# Splunk

An example Splunk dashboard is included in XML format.
