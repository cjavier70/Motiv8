import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/motiv8')

from motiv8 import app as application
application.secret_key = 'cloud computing'

