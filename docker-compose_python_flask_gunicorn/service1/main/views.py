from flask import Flask, request, render_template
from main import app, config
import requests
import logging

#log micro seconds
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', datefmt='%Y-%m-%d %H:%M:%S')


@app.before_request
def log_request_info():
    app.logger.debug('IP: %s', request.remote_addr)
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())
        

@app.route('/', methods=['GET', 'POST'])
def slash():
    if request.method == 'POST':
        variable = request.values.get('variable')
        return variable
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()