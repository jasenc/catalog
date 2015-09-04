#!/usr/bin/python
import sys
import logging
import os

os.environ['DATABASE_URL'] = "postgresql://catalog:udacity@localhost/catalog"
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/")

from catalog import app as application
application.secret_key = "j\x95~XX\xea\x82_]J\x8a\xde\xdf\xb5\x9d\x08>\x83j'\xe3.\xa9\xd3"

