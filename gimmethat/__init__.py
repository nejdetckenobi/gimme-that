#!/usr/bin/env python3

from flask import (Flask, request, url_for, Response,
                   abort, render_template, redirect)
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from gimmethat.config import DefaultConfiguration
from gimmethat.users import check_auth, init_users
from gimmethat.helpers import get_ips
from gimmethat.notifications import (show_start_notification,
                                     show_login_notification,
                                     show_received_notification,
                                     show_scanned_and_received_notification)
from functools import wraps, partial
from datetime import datetime
import werkzeug
import os
from gimmethat.antivirus import scan_file


class ApplicationObject(Flask):
    """docstring for ApplicationObject"""
    def __init__(self, *args, **kwargs):
        super(ApplicationObject, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def start_service(self):
        self.warn_user()
        app.run(host="0.0.0.0", port=app.config['PORT'],
                debug=app.config['DEBUG'], threaded=True)

    def warn_user(self):
        # Console messages
        init_users()
        print('Running with following configuration:')
        if isinstance(self.config['MAX_CONTENT_LENGTH'], int):
            print('Max upload size: {} bytes'.format(
                self.config['MAX_CONTENT_LENGTH']))
        else:
            print('Max upload size: None')
        print('Scan uploaded files:', self.config['SCAN'])
        print('Notifications:', 'ON' if app.config['NOTIFY'] else 'OFF')
        print('You can use the addresses below')
        for ip in get_ips():
            print('\thttp://{}:{}'.format(ip, self.config['PORT']))
        if app.config['NOTIFY']:
            show_start_notification()


app = ApplicationObject(__name__)
app.config.from_object(DefaultConfiguration)
Bootstrap(app)


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
    if app.config['MAX_CONTENT_LENGTH']:
        if total_content_length > app.config['MAX_CONTENT_LENGTH']:
            return abort(413)
    filename = secure_filename(filename)
    file_upl_dir = os.path.join(app.config['UPLOAD_DIR'],
                                request.authorization.username,
                                timestamp)
    if not os.path.exists(file_upl_dir):
        os.makedirs(file_upl_dir, exist_ok=True)
    filepath = os.path.join(file_upl_dir, filename)
    fp = open(filepath, 'wb')
    return fp


@app.route('/')
@requires_auth
def index(data):
    if app.config['NOTIFY']:
        show_login_notification(request.authorization.username)
    return render_template('index.html', title=app.config['TITLE'])


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/', methods=['POST'])
@requires_auth
def upload(data):
    folder_name = data['username']
    if folder_name not in os.listdir(app.config['UPLOAD_DIR']):
        os.makedirs(os.path.join(app.config['UPLOAD_DIR'], folder_name),
                    exist_ok=True)
    print('RECEIVED from "{}"'.format(folder_name))
    timestamp = str(datetime.now()).replace(':', '-')
    stream, form, files = werkzeug.formparser.parse_form_data(
        request.environ,
        stream_factory=partial(
            file_stream_saver,
            timestamp=timestamp))
    files_ok = []
    files_infected = []
    for name, fp in files.items():
        fp.close()
        if app.config['SCAN']:
            abs_filepath = os.path.join(
                app.config['UPLOAD_DIR'], folder_name, timestamp, name)
            scan_results = scan_file(abs_filepath)
            r = scan_results[abs_filepath]
            if r[0] == 'OK':
                files_ok.append(fp.filename)
                print('\t"{}" => {}'.format(fp.filename, r[0]))
            elif r[0] == 'FOUND':
                files_infected.append(fp.filename)
                print('\t"{}" => {} [{}] REMOVED!'.format(
                    fp.filename, r[0], r[1]))
                os.remove(abs_filepath)
            else:
                print('\t"{}" has an interesting scan result. Check below:')
                print(scan_results)
                print('It can be a configuration/permission error',
                      'if you are encountering interesting logs for every',
                      'file.')
        else:
            files_ok.append(fp.filename)
            print('\t"{}"'.format(fp.filename))

    if app.config['NOTIFY']:
        if app.config['SCAN']:
            show_scanned_and_received_notification(
                data['username'],
                files_ok + files_infected,
                files_infected
            )
        else:
            show_received_notification(data['username'], files_ok)

    return redirect(url_for('success'))


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

