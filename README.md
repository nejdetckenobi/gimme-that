# Gimme That

_Gimme That_ is a file transfer tool written in Python. It turns your computer into a server and your friends simply upload their files to your computer! It has a simple web interface. So anyone can use it.

![Peek](https://user-images.githubusercontent.com/4905664/34677327-d15db8ee-f4a0-11e7-898b-a6e01049dba6.gif)


## Installation

I haven't packaged the project yet. But if you want to give it a try, here are the steps:

1. Clone the repo.

    `git clone https://github.com/nejdetckenobi/gimme-that`

2. Go to the project's directory

    `cd gimme-that`

3. Run `make install`

    `make install`

4. Open up `config.py` with your favorite text editor and modify the lines below

| Line  |             Value           |
|-------|-----------------------------|
| TITLE | Message on your upload page. |
| DEBUG | Make it `True` to suppress debug logs (Notice the caps) |
| UPLOAD_DIR | Where to put uploaded files. Use full path and no wildcards. |
| MAX_CONTENT_LENGTH | Total size of files uploaded in a single request in bytes. <br> E.g. `MAX_CONTENT_LENGTH = 50 * 1024 * 1024` for 50 MB. <br> Set it `MAX_CONTENT_LENGTH = None` for unlimited file size. |
| PORT | In default, program uses `5000`. If you want to use another port, set it here. |
| USER_CREDS | Static users' credentials (Username and password). It is a JSON file. |


## How to use it?

Just run `run.py` to run the server. You can find an example gif above. It's the only way because I didn't create standard packages. But later, I'll fix that.

Once you've start the server, your friends can upload files to your computer.
