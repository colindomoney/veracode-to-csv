# Purpose:  Config file for veracode_to_csv.py

# Logging
# debug_logging = True

# Directory to output .csv files
output_directory = "output"

# UTF-8 encoded file containing list of applications to include.
# Note - an empty file will include all application profiles
# app_include_list = "app_include_list.txt"

# Include static/dynamic flaws
include_static_flaws = True
include_dynamic_flaws = True

# Include sandboxes
include_sandboxes = True

# Add headers to csv files
include_csv_headers = True

# Proxy configuration, see http://docs.python-requests.org/en/master/user/advanced/#proxies for options
# proxies = {"https": "http://user:pass@10.10.10.10:8080/"}
