import requests 
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep
os.system('clear')
logo =("""\x1b[1;36m
  _______  _______          
|\     /|(  ___  )(  ____ \|\     /|
| )   ( || (   ) || (    \/| )   ( |
| | _ | || (___) || (_____ | |   | |
\033[1;32m| |( )| ||  ___  |(_____  )| |   | |
| || || || (   ) |      ) || |   | |
| () () || )   ( |/\____) || (___) |
\033[1;32m(_______)|/     \|\_______)(_______)
   
         """
         colors = [GREEN, RED, CYAN, YELLOW, BLUE, MAGENTA]
    box_width = max(len(line) for line in logo_text.split('\n'))
    print(random.choice(colors) + "┌" + "─" * (box_width + 2) + "┐")
    for line in logo_text.split('\n'):
        print(random.choice(colors) + "│ " + line.ljust(box_width) + " │")
    print(random.choice(colors) + "└" + "─" * (box_width + 2) + "┘" + RESET)
    print(Fore.YELLOW + f"[+]WASU MULTI CONVO TOOL")
    print(Fore.YELLOW + f"[+]OWNER:BHAT WASU XWD")
    print(Fore.YELLOW + f"[+]FACEBOOL:WASU INXIDE")
    print(Fore.YELLOW + f"[+]#####################")
    #Login System




while True:

    try:

        print()

        cookies = set_cookie()



        response = make_request('https://business.facebook.com/business_locations', headers={

            'Cookie': cookies,

            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'

        }, cookies={'Cookie': cookies})



        if response is None:

            break



        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)

        id_post = int(input("\033[92mENT3R POST ID :: "))

        commenter_name = get_commenter_name() 

        delay = int(input("\033[92mENT3R D3ALY S3COND3 :: "))  # Bright Green color for input prompt

        comment_file_path = input("\033[92mENT3R YOUR C0MM3NT F1L3 P9TH :: ")  # Bright Green color for input prompt



        # Reading comments from the file

        with open(comment_file_path, 'r') as file:

            comments = file.readlines()



        x, y = 0, 0

        print()



        while True:

            try:

                time.sleep(delay)

                teks = comments[x].strip()

                comment_with_name = f"{commenter_name}: {teks}"  # Add commenter's name to the comment

                data = {

                    'message': comment_with_name,

                    'access_token': token_eaag

                }

                response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookies}).json()

                if '\'id\':' in str(response2):

                    print("\033[92mP0ST ID ::", id_post)  # Post ID

                    print("\033[92mDAT3 T1M3 ::", time.strftime("%Y-%m-%d %H:%M:%S"))  # Date time

                    print("\033[92mBHAT WASU XWD INXIIDE ::", comment_with_name)  # Comment sent with name

                    print('\033[97m' + '################################################################ ')  # Additional line in bright white color

                    x = (x + 1) % len(comments)  # Move to the next comment

                else:

                    y += 1

                    print("\033[91m[{}] Status : Failure".format(y))  # Bright Red color for failure message

                    print("\033[91m[/]Link : https://m.basic.facebook.com//{}".format(id_post))  # Bright Red color for failure message

                    print("\033[91m[/]Comments : {}\n".format(comment_with_name))  # Bright Red color for failure message

                    continue



            except RequestException as e:

                print("\033[91m[!] Error making request:", e)  # Bright Red color for errors

                time.sleep(5.5)

                continue



    except Exception as e:

        print("\033[91m[!] An unexpected error occurred:", e)  # Bright Red color for errors

        break
