import ctypes
import os
ctypes.windll.kernel32.SetConsoleTitleW("Roblox Account Grabber")
print("***Warning!***\nIf you somehow managed to download this program, please change the directory in line 45 and 54 to your own directories. It is set to mine!")
import asyncio
import time
from roblox import Client
from roblox.utilities.exceptions import UserNotFound
from roblox.utilities.exceptions import TooManyRequests
client = Client()
acc = []
try:
    gen = int(input("How many accounts do you want to pull: "))
    print("Amount of accounts that will be generated: "+str(gen))
except ValueError:
    print("Amount of account that will be generated is set to 100 as default. Please eneter a valid integer value next time!")
    gen = 100
try:
    gen2 = int(input("Start ID (12100000 - 12800000): "))
except ValueError:
    print("ID is set to 12745632 as dedault. Please enter a valid integer value next time!")
    gen2 = 12745632
filename = str(input("File Name to save accounts: "))
async def main():
    a=0
    i=0
    idid = gen2
    while i!= gen:
        i += 1
        
        try:
            user = await client.get_user(idid)
            print(user.name + ":l0l0l0l")
            acc.append(user.name +":l0l0l0l")
        except UserNotFound:
            print("Invalid ID")
        except TooManyRequests:
            print("Too many requests, Trying again in 1.5 seconds")
            time.sleep(1.5)
        idid += 1
        a+= 1
    print(str(gen) +" accounts generated!")
    print("Writing all accounts to a file...")
    try:
        with open("C:/Users/adalw/Desktop/usergrabber-main/accounts/" +filename+".txt", 'w') as f:
            for line in acc:
                f.write(line)
                f.write('\n')
    except FileNotFoundError:
        print("Creating account folder")
        time.sleep(0.2)
        print("Writing all accounts to file")
        time.sleep(0.3)
        with open("C:/Users/adalw/Desktop/usergrabber-main/accounts/" +filename+".txt", 'w') as f:
            for line in acc:
                f.write(line)
                f.write('\n')
        os.mkdir("C:/Users/adalw/Desktop/usergrabber-main/accounts")
    print("Writing done!")
    print("Writing last ID to a text file")
    with open("lastid.txt", 'w') as f:
        f.write(str(idid))
    print("Writing done (lastid.txt)")
    print("Closing program in 3 seconds")
    time.sleep(3)
    
        


asyncio.get_event_loop().run_until_complete(main())
