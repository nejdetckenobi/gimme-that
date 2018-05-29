#!/bin/env python3
import argparse
from gimmethat import app
from gimmethat.users import save_creds, load_creds
import os
import re

FILESIZE_PATTERN = re.compile('([0-9]+(\.[0-9]+)?)(.?)')


main_parser = argparse.ArgumentParser(description='Upload server tool')
subparsers = main_parser.add_subparsers(help='What to do?', dest='branch')

run_parser = subparsers.add_parser('run', help='Runs server')
run_parser.add_argument('--port', '-p', type=int,
                        help='Server port')
run_parser.add_argument('--title', '-t', type=str, help='Upload page\'s title')
run_parser.add_argument('--directory', '-d', type=str, help='Upload directory')
run_parser.add_argument('--max-size', '-M', type=str,
                        help='Maximum upload size.')

run_parser.add_argument('--scan', action='store_true',
                        help=('Scan uploaded files with clamav and '
                              'remove the infected ones'))
run_parser.add_argument('--notify', action='store_true',
                        help='Show notifications via notify-osd')
add_user_parser = subparsers.add_parser('add', help='Add a user')
add_user_parser.add_argument('username', type=str, help='User\'s name')
add_user_parser.add_argument('password', type=str, help='User\'s password')

remove_user_parser = subparsers.add_parser('remove', help='Remove a user')
remove_user_parser.add_argument('username', type=str, help='User\'s name')

change_user_parser = subparsers.add_parser(
    'change', help='Change a user\'s password')
change_user_parser.add_argument('username', type=str, help='User\'s name')
change_user_parser.add_argument('password', type=str, help='User\'s password')

show_users_parser = subparsers.add_parser('show', help='Show all users')

args = main_parser.parse_args()

if args.branch == 'run':
    import logging
    log = logging.getLogger(name='werkzeug')
    log.setLevel(logging.INFO)

    if args.max_size:
        num, _, unit = FILESIZE_PATTERN.match(args.max_size).groups()
        num = float(num)
        if not unit:
            pass
        elif unit == 'K':
            num = num * 1024
        elif unit == 'M':
            num = num * 1024 * 1024
        elif unit == 'G':
            num = num * 1024 * 1024 * 1024
        else:
            raise Exception('Unidentified unit \'{}\''.format(unit))

        app.config['MAX_CONTENT_LENGTH'] = int(num)

    if args.scan:
        app.config['SCAN'] = args.scan
    if args.title:
        app.config['TITLE'] = args.title
    if args.directory:
        app.config['UPLOAD_DIR'] = os.path.expanduser(args.directory)
    if args.port:
        app.config['PORT'] = args.port
    app.config['NOTIFY'] = args.notify
    app.start_service()

elif args.branch == 'add':
    creds = load_creds()
    if args.username not in [u['username'] for u in creds]:
        creds.append({'username': args.username,
                      'password': args.password})
        save_creds(creds)
    else:
        print('User already exists.')

elif args.branch == 'remove':
    creds = load_creds()
    creds = [u for u in creds if u['username'] != args.username]
    save_creds(creds)

elif args.branch == 'show':
    creds = load_creds()
    for u in creds:
        print('Username: "{}", Password: "{}"'.format(
            u['username'], u['password']))

elif args.branch == 'change':
    creds = load_creds()
    for u in creds:
        if u['username'] == args.username:
            u['password'] = args.password
    save_creds(creds)
