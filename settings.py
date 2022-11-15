# --------- Flask settings
# Update this for the appropriate front-end website when up
SERVER_HOST = 'https://wwwsite.azurewebsites.net'
SERVER_PORT = 5000
FLASK_DEBUG = True  # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

# -------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

API_URL = "https://azfuncapp2771.azurewebsites.net/api/"
