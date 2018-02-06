from gimmethat.config import DefaultConfiguration
import json
import os


def init_users():
    if not os.path.exists(os.path.expanduser(DefaultConfiguration.UPLOAD_DIR)):
        print('Creating upload directory: {}'.format(
            os.path.expanduser(DefaultConfiguration.UPLOAD_DIR)))
        os.makedirs(os.path.expanduser(DefaultConfiguration.UPLOAD_DIR))

    if not os.path.exists(DefaultConfiguration.USER_CREDS):
        print('Creating credential list : {}'.format(DefaultConfiguration.USER_CREDS))
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


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    users = load_creds()
    for u in users:
        if u['username'] == username and u['password'] == password:
            return True
