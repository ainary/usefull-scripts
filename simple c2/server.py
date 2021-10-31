from flask import Flask, send_file
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/long_random_string/')
def return_files_tut():
    return send_file('config.ovpn', attachment_filename='config.ovpn')

@app.route('/another_long_random_string/')
def rce():
    # change 'no' for desirable command
    return 'no'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='63122', ssl_context=('/etc/letsencrypt/live/domain/fullchain.pem', '/etc/letsencrypt/live/domain/privkey.pem'))