#!/usr/bin/env python
import os
import socket
import subprocess
from termcolor import colored
import platform
import nmap
import requests
import webbrowser
#Zeplin was made by MariusLeVrai

print("""\
███████╗███████╗██████╗ ██╗     ██╗███╗   ██╗
╚══███╔╝██╔════╝██╔══██╗██║     ██║████╗  ██║
  ███╔╝ █████╗  ██████╔╝██║     ██║██╔██╗ ██║
 ███╔╝  ██╔══╝  ██╔═══╝ ██║     ██║██║╚██╗██║
███████╗███████╗██║     ███████╗██║██║ ╚████║
╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
print("[*]Zeplin is a open source advanced terminal for devs[*]")
print("[*]You can configure zeplin into /conf/zeplin.conf[*]")
print("[*]Zeplin Lite 1.0.1[*]\n")
LOCK = True
s = nmap.PortScanner()
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
cwd = os.getcwd()

while LOCK == True:
    prompt = input(f"Zeplin({cwd}) > ")
    prompt = prompt.encode("utf8")
    
    
    
    #commands
    try:
        if len(prompt.decode("utf8")) == 0:
            print(colored("Command is not defined", "red"))
        if prompt.decode("utf8") == "myip":
            print(colored(IPAddr+" as "+hostname+"\n", "green"))
        
        
                
                
        if prompt.decode("utf8") == "run":
            IP = input("(IP) > ")
            print(f"[+]Server ip is set as {IP}[+]")
            PORT = input("(PORT) > ")
            print(f"[+]Server port is set on {PORT}[+]")
            socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.bind((IP, int(PORT)))
            print(f"[+]Server was created by Zeplin[+]")
            print(f"[*]Conf file are into /conf/server.conf[*]")
            print(f"Your server wait on {PORT}...")
            
            while True:
                socket.listen(5)
                conn, address = socket.accept()
                user = conn.recv(1024)
                user = user.decode("utf8")
                print(f"{user} was connected !")
            conn.close()
            socket.close()
        if prompt.decode("utf8") == "bye":
            quit()
        
        if prompt.decode("utf8") == "clear":
                os.system("clear")
        if prompt.decode("utf8") == "inf":
                print(colored("System : "+platform.system(), "green"))
                print(colored("Architecture : "+platform.machine(), "green"))
                print(colored("Release : "+platform.release(), "green"))
                print(colored("Pyhton : "+platform.python_version()+"\n", "green"))
        if prompt.decode("utf8") == "reload":
                os.system("python3 main.py")
                os.system("clear")
        if prompt.decode("utf8") == "r":
            url = input("(url) > ")
            r = requests.get(url)
            print(f"\n{r.headers}")
        if prompt.decode("utf8") == "ver":
            print(colored("Zeplin Lite 1.0.1 x86_x64\n", "green"))
        if prompt.decode("utf8") == "get":
            url = input("(url) > ")
            r = requests.get(url)
            print(f"\n{r.text}")
        
        if prompt.decode("utf8") == "search":
            url = input("(url) > ")
            webbrowser.open(url)
        if prompt.decode("utf8") == "download":
            url = input("(url) > ")
            name= input("(name) > ")
            response = requests.get(url, allow_redirects=True)
            string = response.text
            open("download/"+name, "w").write(str(string))
        if prompt.decode("utf8") == "h":
            print(colored("myip : get your local ip and hostname of your pc\nrun : to launch a server with socket\nbye : to quit the terminal\ninf : to get info of your system\nreload : restart the script\nr : send a custom request\nver : get the version of zeplin\nget : get the html code of a website\nsearch : open a url into browser\ndownload : download a file from the web with url\nupdate : update zeplin", "green"))
        if prompt.decode("utf8") == "update":
            os.system("rm *.*")
            os.system("git clone https://github.com/mariuslevrai/zeplin")
            
    
        
    
    finally:
        os.system(prompt.decode("utf8"))