﻿# Gimme That

_Gimme That_ is a file transfer tool written in Python. It turns your computer into a server and your friends simply upload their files to your computer! It has a simple web interface. So anyone can use it.

![Peek](https://user-images.githubusercontent.com/4905664/34677327-d15db8ee-f4a0-11e7-898b-a6e01049dba6.gif)


## Installation

Just use `pip install gimmethat` to install.
It has following Python package dependencies

- `flask`
- `flask_bootstrap`
- `netifaces`
- `clamd`

## How to use it?

_Gimme That_ has a simple concept: You turn yourself into a server, add some username and password, give that credentials to your friend with your adress and your friend uploads files to your computer.

So, there are several things you can do with this program.

### Creating users

Use the line below to create a user named *USER* with the password *PASSWORD*

`gimme add USER PASSWORD`


### Removing users

Use the line below to remove a user named *USER*

`gimme remove USER`


### Changing user passwords

Use the line below to change *USER*'s password to *PASSWORD*

`gimme change USER PASSWORD`

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
| `--directory` | `"~/Uploads"` (`~` is current user's home directory in both Windows and *nix) |
| `--port` | 5000 |
| `--title` | `""` (Nothing will be shown as title) |
| `--max-size` | No limit if not set. <br> Can be `256` for 256 bytes, <br> `13.6K` for 13.6 kilobytes, <br> `1M` for 1 megabyte, <br> `2.2G` for 2.2 gigabytes, <br> etc. |
| `--scan` | False if not specified. Else, <br> uploaded files will be scanned if you have ClamAV <br> and will be removed if infected. |

## Notes

- *GimmeThat* uses [Twitter's Bootstrap](https://getbootstrap.com/).

- *GimmeThat* **does not overwrite** uploaded files. When your friend `user` used your server to upload `wiggle.jpg` at `2018-01-17 16:14:24.620737`, program will put the files into `~/Uploads/user/2018-01-17 16-14-24.620737/wiggle.jpg`. So, even if he/she uploads the same file again and again, it'll be put into different directories.

- You can drop files. It has drag and drop support.

- If you specify `--scan` option and getting interesting logs for every single file (or an error maybe), you may have the issues below:
  Both issues are solved for linux. Please check [Antivirus Issues](#antivirus-issues) section.
  - Clamav is not installed.
  - Permission errors. (Possible cause of `lstat() failed`)

## Additional Screenshots

Command line while a client uploads some files, ClamAV's action when an infected file found, multi file uploading and removing infected ones while clean ones stay.

![antivirus](https://user-images.githubusercontent.com/4905664/35181654-f3143e10-fdd6-11e7-8b67-9f7e834e87dc.gif)



## Antivirus Issues

### Clamav is not installed

**Note:** For CentOS, please follow [this tutorial](https://linux-audit.com/install-clamav-on-centos-7-using-freshclam/) then take the [hard way](#hard-way). The commands below will not work for you obviously till the hard way.

Please use the command below to install ClamAV:

```sh
sudo apt-get install clamav-daemon clamav-freshclam clamav-unofficial-sigs
```

Then update the virus DB by running the commands below. This will take some time.

```sh
sudo systemctl stop clamav-daemon
sudo systemctl stop clamav-freshclam
sudo freshclam  # It'll update the virus DB.
```

And then start ClamAV daemon:

```sh
sudo systemctl start clamav-daemon
sudo systemctl start clamav-freshclam
```

Optionally, you enable `clamav-daemon` so it will be automatically run on startup:

```sh
sudo systemctl enable clamav-daemon
sudo systemctl enable clamav-freshclam
```

### Clamav is not configured properly

#### Easy way

Linux users uses Debian/Ubuntu based distros, after the installation, run `gimmeconf` and you should be OK.
For all else - or if you're not OK with that - you should try the hard way.


#### Hard way

I am assuming that you reinstalled the following packages:
(If you didn't, please try reinstalling the packages.)

- clamav-daemon
- clamav-freshclam
- clamav-unofficial-sigs

**Note:** `USERNAME` is your account's username. **Not** the name which you created with `gimme add`.

Stop the ClamAV first:
```sh
sudo systemctl stop clamav-daemon
sudo systemctl stop clamav-freshclam
```

Just because I use ClamAV for on-demand scans, I set the user for ClamAV as ourselves.
To do this, open `/etc/clamav/clamd.conf` with your text editor and find the `User` line.
(**Caution**: It will require superuser privileges.)

```
...
User clamav
...
```
Replace the value `clamav` with your username. (My username is `USERNAME` here.)

```
User USERNAME
```

Save and close the file when you're done.

Add your user to `clamav` group.

```sh
sudo adduser USERNAME clamav
```

Then change the ownership of the log file so it can use the file again

```sh
sudo chown USERNAME:clamav /var/log/clamav/clamav.log
```

And lastly, start ClamAV again:
```sh
sudo systemctl start clamav-daemon
```

## Thanks

Thanks to the following reddit users for their ideas:

- [AyrA_ch](https://www.reddit.com/user/AyrA_ch)
- [RibMusic](https://www.reddit.com/user/RibMusic)
