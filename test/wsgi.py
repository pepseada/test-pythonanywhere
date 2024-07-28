import os
import sys

# Path to your Django project directory
path = '/home/seada/test-pythonanywhere'
if path not in sys.path:
    sys.path.append(path)

# Path to the directory containing the settings module
sys.path.append('/home/seada/test-pythonanywhere/test')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'

# Import and set up the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
