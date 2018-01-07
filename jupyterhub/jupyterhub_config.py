import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.MyOAuthenticator.oauth_callback_url = '/hub/oauth_callback'
c.MyOAuthenticator.client_id = open(os.environ['OAUTH_CLIENT_ID_PATH']).read().strip()
c.MyOAuthenticator.client_secret = open(os.environ['OAUTH_CLIENT_SECRET_PATH']).read().strip()
logger.debug("ID: " + c.MyOAuthenticator.client_id)
logger.debug("SECRET: " + c.MyOAuthenticator.client_secret)

c.JupyterHub.ip = '0.0.0.0'
