import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

import time
import discord
import asyncio
import codecs
import sys
import io
import threading
import requests
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore, init 
import random

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

JANKY = commands.Bot(command_prefix='-', self_bot=True)
JANKY.remove_command("help")

print(f'''{Fore.RED}

███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗    
████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║    
██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║    
██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║    
██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║    
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝    
                                                              
                                                        
__________________________________________________________                                                                                                                             

{Fore.RED}[+] MADE BY JANKY
{Fore.RED}[+] FREE TO USE FOR EVERYONE      
{Fore.RED}[+] DONT JUST SKID GIVE CREDITS

{Fore.RED}__________________________________________________________       ''')

print(f'''{Fore.RED}

              ENTER A TOKEN TO MASS-DM        

{Fore.RED}__________________________________________________________                                     ''')                                                                                      
                                                                              
token = input(f'''{Fore.GREEN}
              TOKEN :                                                        ''')
                                                                               
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
print('')
if src.status_code == 200:
    print('             [+] Account valid. ')
    print('__________________________________________________________ ')
    print('')
else:
    print(f'[{Fore.RED}-{Fore.RESET}] [-] Token invalid.')
    input("Press any key to exit...")
    exit(0)


print(f'''{Fore.GREEN}             [𝟭] - MASS DM ''')
print('\n')

def MASSDM(token):

    @JANKY.event
    async def on_ready():
        print('DMING ALL ALL...')
    
        for user in JANKY.user.friends:
            try:
                time.sleep(5)
                await user.send("PUT WHATEVER YOU WANT HERE")
                print(f'MESSAGE SENT TO : {user}')
            except:
                print(f"MESSAGE COULD NOT BE SENT TO : {user}")
        
        print('\n')
        print('FINISHED SENDING MESSAGES')
        print('TO SEND MESSAGES AGAIN RESTART THE BOT')
        print('\n')
    JANKY.run(token, bot=False)

def mainanswer():
    answer = input('             PICK 1 : ')
    if answer == '1':
        MASSDM(token)

mainanswer()