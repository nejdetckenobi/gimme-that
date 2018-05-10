import os


class DefaultConfiguration(object):
    # Debugging purposes
    DEBUG = False
    BOOTSTRAP_SERVE_LOCAL = True

    # The line below is where to put the uploaded files.
    # Use the full path and do not use wildcards.
    # ~ is user's home directory
    UPLOAD_DIR = os.path.expanduser("~/Uploads")

    # You can rewrite the key. Don't forget the quotes
    SECRET_KEY = "#VERY_HARD_KEY#"

    # The line below keeps the user list.
    USER_CREDS = os.path.expanduser("~/gimmethat_userlist.json")

    TITLE = ''

    # Biggest file size in bytes.
    MAX_CONTENT_LENGTH = None

    # Antivirus enabled
    SCAN = False

    # Port
    PORT = 5000

    # Notify
    NOTIFY = False
