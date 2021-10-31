import requests
import random
import string
import subprocess
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

http = requests.Session()
retries = Retry(total=10, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
http.mount("https://", HTTPAdapter(max_retries=retries))

def download_conf():

    url = 'https://domain_name/long_random_string/'
    data = http.get(url)
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    filename = "/tmp/"+ random_string + ".ovpn"
    with open(filename, 'wb')as file:
        file.write(data.content)
    subprocess.Popen(["/usr/sbin/openvpn","--config", filename])

download_conf()