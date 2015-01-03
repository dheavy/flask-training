import os
import config_local


basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'

OPENID_PROVIDERS = [
  { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
  { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
  { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
  { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
  { 'name': 'MyOpenID', 'url': 'https://www.openid.com' }
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Mail server settings.
MAIL_SERVER = config_local.MAIL_SERVER
MAIL_PORT = config_local.MAIL_PORT
MAIL_USERNAME = config_local.MAIL_USERNAME
MAIL_PASSWORD = config_local.MAIL_PASSWORD

# Admin list.
ADMINS = ['hello@davybraun.com']

# Pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
