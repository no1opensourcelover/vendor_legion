# Authored By : @https://t.me/Immanuel_Raj

# Imports
import os
import sys
from os import path

# OTA
def ota():
    print ("\nMoving to OTA repository\n")
    os.chdir("OTA")
    print("\nUnshallowing the repository\n")
    os.system("git fetch LegionOS-Devices --unshallow")
    os.system("git checkout 11")
    os.system("git pull LegionOS-Devices 11")
    print ("")
    print ("Device directory exists : " + str(path.exists(codename)))
    result=path.exists(codename)
    if result==False:
        print("\nCreating the device folder... xd\n")
        os.system("mkdir %s"%codename)
        os.chdir("%s"%codename)
        os.system("mkdir official")
        print("\nFolder created succesfully... xd\n")
        print("\nCreating the necessary files... xd\n")
        os.mknod("changelogs_gapps.txt")
        os.mknod("changelogs_vanilla.txt")
        os.chdir("official")
        os.mknod("gapps.json")
        os.mknod("vanilla.json")
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        print("\nCreating the necessary files completed succesfully... xd\n")
        print("\nHey new maintainer!!! welcome to the Project LegionOS hope you have a great time here\n")
        print("\nContinuing the script....xd\n")
        os.system("bash ota.sh %s %s"%(codename,variant))
        print ("")
    else:
        os.chdir("..")
        print("\nContinuing the script....xd\n")
        os.system("bash ota.sh %s %s"%(codename,variant))
        print ("")

# Banner
print ("")
print ("-----------------------------------------------")
print ("")
print("""
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳━━━╮
┃╭━╮┃╱╱╱╱╭╮╱╱╱╱╭╯╰╮╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╭━╮┃
┃╰━╯┣━┳━━╋╋━━┳━┻╮╭╯╱┃┃╱╱╭━━┳━━┳┳━━┳━╮┃┃╱┃┃╰━━╮
┃╭━━┫╭┫╭╮┣┫┃━┫╭━┫┣━━┫┃╱╭┫┃━┫╭╮┣┫╭╮┃╭╮┫┃╱┃┣━━╮┃
┃┃╱╱┃┃┃╰╯┃┃┃━┫╰━┫╰┳━┫╰━╯┃┃━┫╰╯┃┃╰╯┃┃┃┃╰━╯┃╰━╯┃
╰╯╱╱╰╯╰━━┫┣━━┻━━┻━╯╱╰━━━┻━━┻━╮┣┻━━┻╯╰┻━━━┻━━━╯
╱╱╱╱╱╱╱╱╭╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱""")
print ("")
print ("-----------------------------------------------")
print ("")
print ("ONLY FOR OFFICIAL BUILDS/USE")
print ("")
print ("")
print ("")

# Variables
codename=input("\nEnter your device code name :- eg miatoll/laurel_sprout : ")

# Checks
check1 = open("devices.json", "r")
check2 = open("legion.devices", "r")
store1 = check1.read()
store2 = check2.read()
if codename in store1:
    if codename in store2:
        print("\nChecks passed\n")
else:
    print("\nFor official devices only\n\nExiting.....\n")
    sys.exit()

# Variables
sfun=input("\nEnter your sourceforge username :-  ")
sfpass=input("\nEnter your sourceforge password : ")
btype=input("\nEnter the type of build u want [user/eng/userdebug] : ")

# Deps
os.system("sudo apt-get install sshpass -y")

# Variant & Building & OTA
variant=str("gapps")
os.system("bash build.sh %s true %s"%(codename,btype))
os.system("sshpass -p '%s' rsync --progress out/target/product/%s/LegionOS*.zip %s@frs.sourceforge.net:/home/frs/project/legionrom/%s/"%(sfpass,codename,sfun,codename))
ota()
variant=str("vanilla")
os.system("bash build.sh %s false %s"%(codename,btype))
os.system("sshpass -p '%s' rsync --progress out/target/product/%s/LegionOS*.zip %s@frs.sourceforge.net:/home/frs/project/legionrom/%s/"%(sfpass,codename,sfun,codename))
ota()

# Telegram notification
print("\nPosting in Telegram....\n")
codename=input("\nEnter your device code name :- eg miatoll/laurel\_sprout : ")
tgun=input("\nPlease type your telegram username (without @) username or user\_name : ")
device=input("\nEnter your device name (Xiaomi Mi A2) : ")
legv=input("\nEnter LegionOS Verison(2.8/3.9) : ")
patch=input("\nEnter security patch date (May 2021) :  ")
os.system("bash tg.sh '%s' '%s' '%s' '%s' '%s'"%(device,legv,codename,patch,tgun))
print("\nPosted in Telegram\n")
print("\nExiting...\n")
print("\nBye have a great day\n")
