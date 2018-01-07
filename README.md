This is just to demonstrate how to use ```django-oauth-toolkit``` to serve as an authenticator for jupyterhub. Please note that this is in no way geared toward being operational or deployable. There is no security added to this app. It is intended purely as a minimal example of OAuth2 integration between Jupyterhub and Django.

To make this deployment easier, I've pre-generated an admin user, and oauth client id and secret. The user is:

Username: admin

Password: adminadmin

and the oauth strings are hard-coded into the jupyterhub. Django uses a sqlite database included with this repository to make this easily reproducible.

To test this, just run:

    docker-compose up --build

The sample web app will be served on port 8000, and the jupyterhub will be on 8001.
