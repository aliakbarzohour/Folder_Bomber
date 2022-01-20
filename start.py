# import librar's
import os
from rand_string.rand_string import RandString
from colorama import Fore, init

# start coding folder bomber main
print(" 😈 Let's Go . . .")

count = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"How mony time's ? :  "))
# define lenght for directory name's
lenght = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"lenght ? : "))

for i in range(0, count):
    # making directory
    os.mkdir(RandString("uppercase", lenght))
    # print Result
    print(Fore.RED+" [$] "+Fore.WHITE+"Making Folder :: ", i, "\n")

print(" 🩸 End . . .")
