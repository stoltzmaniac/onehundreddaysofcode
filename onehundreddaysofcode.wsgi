#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/onehundreddaysofcode/")

from autoapp import app as application
from onehundreddaysofcode.settings import SECRET_KEY
application.secret_key = SECRET_KEY