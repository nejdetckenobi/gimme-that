#!/bin/env python3
from app import app, USER_CREDS, PORT
from config import DEBUG, UPLOAD_DIR
import os


if __name__ == '__main__':
    if not DEBUG:
        import logging
        log = logging.getLogger(name='werkzeug')
        log.setLevel(logging.INFO)

    if not os.path.exists(UPLOAD_DIR):
        os.mkdir(UPLOAD_DIR)
    if not os.path.exists(USER_CREDS):
        with open(USER_CREDS) as f:
            pass

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG, threaded=True)
