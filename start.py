# import librar's
import os
from rand_string.rand_string import RandString
from colorama import Fore

# start coding folder bomber main
print(" 😈 Let's Go . . .")

# define counter for making directory
count = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"How mony time's ? :  "))
# define lenght for directory name's
lenght = int(input(Fore.YELLOW+" [?] "+Fore.WHITE+"lenght ? : "))
# -------------------------------------------------------------------------
# I'm building this loop to both have better control over the construction
# of the routes and to be able to reduce my code.
# -------------------------------------------------------------------------
for i in range(0, count):
    # making directory
    os.mkdir(RandString("uppercase", lenght))
    # print Result
    print(Fore.RED+" [$] "+Fore.WHITE+"Making Folder :: ", i, "\n")
# -------------------------------------------------------------------------
# This text also runs at the end of this program.
# If this section is printed for you, you can be
# sure that the program is running!
# -------------------------------------------------------------------------
print(" 🩸 End . . .")
