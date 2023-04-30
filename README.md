# Bruteforcer-qdPM
This is a simple credential bruteforcer for qdPM.
It is tested against version 9.1 on [Vulnhub - CheesyJack](https://www.vulnhub.com/entry/cheesey-cheeseyjack,578/) and a walkthrough exercise for offsec pen200.
This script is created during the pen 200 course since Hydra did not find the correct credentials. When I tried it with Burp Suite Intruder I could find the correct credentials. Based on this experience I decided to create a simple bruteforce script to get the correct credentials for qdPM (9.1). This script is tested agains the two mentioned test machines in an educational environment. This script probabbly works against version 9.2 as well.

Usage:
```
python3 Bruteforcer-qdPM-9-1.py -url http://10.0.2.42/project_management/ -u users.txt  -p passwords.txt
```
There are three arguments to run the script:
* The `-url` to identify the root of qdPM
* The `-u`  to identify the list with email-addresses as usernames
* The `-p` to identify the list with possible passwords

![Bruteforcer qdPM 9-1](https://github.com/eMVee-NL/Bruteforcer-qdPM/blob/main/Images/Bruteforcer-qdPM-9-1.png?raw=true)
