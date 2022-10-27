from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# When deploying to Azure App Service, add you <name>.azurewebsites.net 
# domain to ALLOWED_HOSTS; you get an error message if you forget. When you add
# a specific host, you must also add 'localhost' and/or '127.0.0.1' for local
# debugging (which are enabled by default when ALLOWED_HOSTS is empty.)
# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

try:
    from .local import *
except ImportError:
    pass