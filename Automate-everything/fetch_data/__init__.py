import ssl
import urllib3
from pynetbox import api
import requests
from config import nb, token

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()

session = requests.Session()
session.verify = False

netbox_session = api(nb, token=token)
netbox_session.http_session = session

def get_netbox_session():
    return netbox_session
