from flask import (Flask, request, url_for, Response,
                   abort, render_template, redirect)
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from gimmethat.config import UPLOAD_DIR, SECRET_KEY, USER_CREDS
from functools import wraps, partial
from datetime import datetime
import werkzeug
import netifaces as ni
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['UPLOAD_DIR'] = UPLOAD_DIR
app.config['TITLE'] = ''

Bootstrap(app)


def get_ips():
    interfaces = ni.interfaces()
    ips = []
    for interface in interfaces:
        try:
            if 'broadcast' in ni.ifaddresses(interface)[ni.AF_INET][0]:
                ips.append(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
        except KeyError:
            pass
    return ips


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    with open(USER_CREDS) as f:
        users = json.load(f)
    for u in users:
        if u['username'] == username and u['password'] == password:
            return True


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return Response(
                render_template('unauthorized.html'), 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(data={'username': auth.username,
                       'time': datetime.now()}, *args, **kwargs)
    return decorated


def file_stream_saver(total_content_length, content_type, filename,
                      content_length=None, timestamp='NONE'):
    if total_content_length > app.config['MAX_CONTENT_LENGTH']:
        return abort(413)
    filename = secure_filename(filename)
    file_upl_dir = os.path.join(UPLOAD_DIR,
                                request.authorization.username,
                                timestamp)
    if not os.path.exists(file_upl_dir):
        os.mkdir(file_upl_dir)
    filepath = os.path.join(file_upl_dir, filename)
    fp = open(filepath, 'wb')
    return fp


@app.route('/')
@requires_auth
def index(data):
    return render_template('index.html', title=app.config['TITLE'])


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/upload', methods=['POST'])
@requires_auth
def upload(data):
    folder_name = data['username']
    if folder_name not in os.listdir(UPLOAD_DIR):
        os.mkdir(os.path.join(UPLOAD_DIR, folder_name))
    print('RECEIVED from "{}"'.format(folder_name))
    stream, form, files = werkzeug.formparser.parse_form_data(
        request.environ,
        stream_factory=partial(
            file_stream_saver,
            timestamp=str(datetime.now()).replace(':', '-')))
    for fp in files.values():
        print('\t"{}"'.format(fp.filename))
        fp.close()
    return redirect(url_for('success'))


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
