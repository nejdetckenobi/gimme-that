# Gimme That

_Gimme That_ is a file transfer tool written in Python. It turns your computer into a server and your friends simply upload their files to your computer! It has a simple web interface. So anyone can use it.

![Peek](https://user-images.githubusercontent.com/4905664/34677327-d15db8ee-f4a0-11e7-898b-a6e01049dba6.gif)


## Installation

Just use `pip install gimmethat` to install. 
It has following dependencies

- `flask`
- `flask_bootstrap`
- `netifaces`

## How to use it?

_Gimme That_ has a simple concept: You turn yourself into a server, add some username and password, give that credentials to your friend with your adress and your friend uploads files to your computer.

So, there are several things you can do with this program.

### Creating users

Use the line below to create a user named *USERNAME* with the password *PASSWORD*

`gimme add USERNAME PASSWORD`


### Removing users

Use the line below to remove a user named *USERNAME*

`gimme remove USERNAME`


### Changing user passwords

Use the line below to change *USERNAME*'s password to *PASSWORD*

`gimme change USERNAME PASSWORD`

### Showing all users

You can see all users you created by typing

`gimme show`

### Running the server

Use the command below to run your server on port *PORT*

`gimme run`

This will produce the output which contains the address of the interfaces you can use to connect the upload page. 
Once you've start the server, your friends can upload files to your computer. Please use `Python 3.x`.
You can specify port, title and upload directory by using optional parameters.
For example, to provide the screen above and to set upload directory to *SOMEPATH*, you should use the command below

`gimme run --port 5000 --directory "SOMEPATH" --title "Someone's file storage"`

#### Default values for parameters

| Name | Value |
|------|-------|
| `--directory` | `~/Uploads` (`~` is current user's home directory in both Windows and *nix) |
| `--port` | 5000 |
| `--title` | `` (Nothing will be shown as title) | 

## Notes

- *GimmeThat* uses [Twitter's Bootstrap](https://getbootstrap.com/).

- *GimmeThat* **does not overwrite** uploaded files. When your friend `user` used your server to upload `wiggle.jpg` at `2018-01-17 16:14:24.620737`, program will put the files into `~/Uploads/user/2018-01-17 16:14:24.620737/wiggle.jpg`. So, even if he/she uploads the same file again and again, it'll be put into different directories.
