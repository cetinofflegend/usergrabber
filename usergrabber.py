import asyncio
from roblox import Client
from roblox.utilities.exceptions import UserNotFound
client = Client()
loop = asyncio.get_event_loop()
acc = []
async def main():
    a=0
    i=3
    idid = 12100000
    while i< 5:
        
        try:
            user = await client.get_user(idid)
            print(user.name)
            acc.append(user.name)
            if a == 100:
                with open('readme.txt', 'w') as f:
                    for line in acc:
                        f.write('\n')
                        f.write(line)
                        f.write('\n')
                acc.clear()
                a = 0
        except UserNotFound:
            print("User not found")
        idid += 1
        a+= 1


loop.run_until_complete(main())