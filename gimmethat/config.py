import os

# Debugging purposes
DEBUG = False

# The line below is where to put the uploaded files.
# Use the full path and do not use wildcards.
# ~ is user's home directory
UPLOAD_DIR = os.path.expanduser("~/Uploads")

# You can rewrite the key. Don't forget the quotes
SECRET_KEY = "#VERY_HARD_KEY#"

# The line below keeps the permanent user list.
USER_CREDS = os.path.expanduser("~/gimmethat_userlist.json")
