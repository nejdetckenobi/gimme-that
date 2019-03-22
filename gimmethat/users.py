from gimmethat.config import DefaultConfiguration
from hashlib import sha1
import json
import os


def init_users():
    if not os.path.exists(os.path.expanduser(DefaultConfiguration.UPLOAD_DIR)):
        print('Creating upload directory: {}'.format(
            os.path.expanduser(DefaultConfiguration.UPLOAD_DIR)))
        os.makedirs(os.path.expanduser(DefaultConfiguration.UPLOAD_DIR))

    if not os.path.exists(DefaultConfiguration.USER_CREDS):
        print('Creating credential list : {}'.format(DefaultConfiguration.USER_CREDS))  # NOQA
        save_creds()


def save_creds(creds=None):
    if not creds:
        creds = []
    with open(DefaultConfiguration.USER_CREDS, 'w') as f:
        json.dump(creds, f, indent=4)


def load_creds():
    try:
        with open(DefaultConfiguration.USER_CREDS) as f:
            creds = json.load(f)
        return creds
    except Exception:
        save_creds()
    return []


def hash_password(password):
    return sha1(password.encode('utf-8')).hexdigest()


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    users = load_creds()
    for u in users:
        candidate_sha = hash_password(password)
        if u['username'] == username and u['password'] == candidate_sha:
            return True
    return False


def add_cred(username, password):
    """
    This function is called to add a new user credential
    """
    users = load_creds()
    if username not in [u['username'] for u in users]:
        users.append({'username': username,
                      'password': hash_password(password)})
        save_creds(users)
        return True
    return False


def remove_cred(username):
    users = load_creds()
    try:
        index = [u['username'] for u in users].index(username)
    except ValueError:
        return False
    users.pop(index)
    save_creds()
    return True


def change_password(username, password):
    users = load_creds()
    try:
        index = [u['username'] for u in users].index(username)
    except ValueError:
        return False

    users[index]['password'] = hash_password(password)
    save_creds(users)
    return True
