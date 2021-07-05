from datetime import datetime
import requests
import json
from colorama import *
from termcolor import colored
import os
from time import sleep
init()
print(colored("""                      
 /_ _  _  /__  _  _  /_
/_//_|/_ /\/_//_|/_ /\ 
          /            
  _                    
  _/  _  /_ _  _       
._/  /_ / //_|/        
                       
                   
_/__  _  /             
/ /_//_//              
                                         
""", 'cyan'))


print("\nInstalling required dependencies...\n")
os.system("pip install mcsniperpy")
while True:
    print("\n")
    response = input("""What would you like to view?
    [1] Upcoming 3 Character Names
    [2] Next 3 Character Name To Drop
    [3] Snipe Next 3 Character Username
    [4] Auto-Snipe All 3 Character Usernames Coming Up (Leave Program Open)
    [5] View Next Available 3 Char on NameMC\n""")

    r = requests.get("http://api.coolkidmacho.com/three") 
    rjson = r.json()
    rtext = r.text

    if response == '1':
        w = 0
        r = 1
        print("\n")

        while r < 6: 
            print(rjson[r]['name'] + ' drops at: ')
            ts = int((rjson[r]['droptime']))
            print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + "\n")
            r += 1
            w = 0

    if response == '2':
        print("\n")
        print(rjson[1]['name'] + ' drops at: ')
        ts = int(rjson[1]['droptime'])
        print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    if response == '3':
        print("Loading MCSniperPY...")
        sleep(1.3)
        current3char = rjson[0]["name"]
        print("If you have never used MCSniperPY before, please type your accounts in accounts.txt file.")
        sleep(2)
        delay = input("What delay would you like to snipe names with?\n")
        os.system(f"mcsniperpy snipe --username {current3char} --offset {delay}")
    if response == '4':
        print("Loading MCSniperPY...")
        sleep(1.3)
        while True:
            r = requests.get("http://api.coolkidmacho.com/three") 
            rjson = r.json()
            rtext = r.text
            current3char = rjson[0]["name"]
            print("If you have never used MCSniperPY before, please type your accounts in accounts.txt file.")
            sleep(2)
            delay = input("What delay would you like to snipe names with?\n")
            os.system(f"mcsniperpy snipe --username {current3char} --offset {delay}")
            print("\nSniping Next Name.\n")
    if response == '5':
        