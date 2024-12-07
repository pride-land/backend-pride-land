#!/home/xs374324/anaconda3/bin/python
# encoding: utf-8

import sys, os
from flup.server.fcgi import WSGIServer

# Add your project directory to the Python path
sys.path.append("/home/xs374324/pridefarm.org/public_html/")

# Add the virtual environment's site-packages to the Python path
venv_path = "/home/xs374324/pridefarm.org/public_html/venv/lib/python3.12/site-packages"
sys.path.insert(0, venv_path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"

# Import and run the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
WSGIServer(application).run()
