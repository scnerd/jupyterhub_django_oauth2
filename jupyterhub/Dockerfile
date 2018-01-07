FROM jupyterhub/jupyterhub

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]