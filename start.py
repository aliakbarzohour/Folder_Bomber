# import librar's 
import os
from rand_string.rand_string import RandString
from colorama import Fore,init

# start coding folder bomber main
print(" 😈 Let's Go . . .")

count = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"How mony time's ? :  "))

for i in range(0, count):
    lenght = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"lenght ? : "))
    os.mkdir(RandString("uppercase", lenght))
    print(Fore.RED+" [$] "+Fore.WHITE+"Making Folder :: ",i,"\n")

print(" 🩸 End . . .")