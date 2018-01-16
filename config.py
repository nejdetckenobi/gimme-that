import os

# Cosmetic
TITLE = "Someone's file storage"

# Debugging purposes
DEBUG = False

# The line below is where to put the uploaded files.
# Use the full path and do not use wildcards.
UPLOAD_DIR = os.path.expanduser("~/Uploads")

# Total file size in one upload session.
# e.g.
# "MAX_CONTENT_LENGTH = 50 * 1024 * 1024" means 50MB
# "MAX_CONTENT_LENGTH = None" means no max file upload limit )
MAX_CONTENT_LENGTH = None

# You can rewrite the key. Don't forget the quotes
SECRET_KEY = "#VERY_HARD_KEY#"

# You can change the port. Do not use ports smaller than 1000.
PORT = 5000

# The line below keeps the permanent user list.
USER_CREDS = "userlist.json"
