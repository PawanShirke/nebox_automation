import ssl 
import urllib3
from config import nb, token
from pynetbox import api
from jinja2 import Environment, FileSystemLoader
import requests

ssl._create_defautl_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()

session = requests.Session()
session.verify = False

netbox_session = api(nb, token=token)
netbox_session.http_session = session

def get_netbox_session():
    # Make a request to the API to check the connection
    response = session.get(nb, headers={"Authorization": f"Token {token}"})
    
    if response.status_code == 200:
        print("Successfully connected to NetBox API.")
        print(":-)")
        return netbox_session
    else:
        print(f"Failed to connect to NetBox API. Status code: {response.status_code}")
        print(":(")
        return None