# Authored By : @https://t.me/Immanuel_Raj

# Imports
import os
import sys
import subprocess
from os import path

# Check out dir for file's existence
def checkout():
    os.chdir("out/target/product/%s"%codename)
    print("")
    findf=os.system("find LegionOS*.zip")
    res=path.exists(findf)
    if res==False:
        print("\nFile Not found in out folder there maybee some build errros\n")
        print("\nDo check for errors and rebuild\n")
        sys.exit()
    else:
        os.chdir("../../../..")
        print("\nOutput file found continuing to upload the file\n")

# OTA
def ota():
    print ("\nMoving to OTA repository\n")
    os.chdir("OTA")
    print("\nUnshallowing the repository\n")
    if ghun!="IMMANUEL44" or "rajkale99" or "anonhacker47" or "lucasponez" or "CrisBalGreece":
        os.system("git remote add LegionOS-Devices https://github.com/%s/OTA"%ghun)
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
        os.chdir("%s"%official)
        os.system("mkdir web")
        os.chdir("..")
        os.chdir("..")
        print("\nFolder created succesfully... xd\n")
        print("\nCreating the necessary files... xd\n")
        os.mknod("changelogs_gapps.txt")
        os.mknod("changelogs_vanilla.txt")
        os.chdir("official")
        os.chdir("web")
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
print ("Make sure to run username@frs.sourceforge.net once before using the script")

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

# Deps
print("\nChecking if sshpass is already installed")
depp = subprocess.check_output(['apt', 'list', '--installed', 'sshpass'])
if "sshpass" in str(depp):
    print("Cool, sshpass is installed so lets continue\n")
    pass
else:
    print("\nPlease consider installing it then run the program again\n")
    sys.exit()

# Variables
sfun=input("\nEnter your sourceforge username :-  ")
sfpass=input("\nEnter your sourceforge password : ")
btype=input("\nEnter the type of build u want [user/eng/userdebug] : ")
tgun=input("\nPlease type your telegram username (without @) : ")
ghun=input("\nEnter your Github username :-  ")
kbu=input("\nEnter name for KBUILD_BUILD_USER :- ")
if "_" in tgun:
    c=tgun.replace("_","\_")
    tgun=c
device=input("\nEnter your device name (Xiaomi Mi A2) : ")
legv=input("\nEnter LegionOS Verison(2.8/3.9) : ")
patch=input("\nEnter security patch date (May 2021) :  ")
print("")

# Variant & Building & OTA
variant=str("gapps")
os.system("bash build.sh %s true %s %s"%(codename,btype,kbu))
checkout()
os.system("sshpass -p '%s' rsync --progress out/target/product/%s/LegionOS*.zip %s@frs.sourceforge.net:/home/frs/project/legionrom/%s/"%(sfpass,codename,sfun,codename))
ota()
variant=str("vanilla")
os.system("bash build.sh %s false %s %s"%(codename,btype,kbu))
checkout()
os.system("sshpass -p '%s' rsync --progress out/target/product/%s/LegionOS*.zip %s@frs.sourceforge.net:/home/frs/project/legionrom/%s/"%(sfpass,codename,sfun,codename))
ota()

# Telegram notification
print("\nPosting in Telegram....\n")
if "_" in codename:
    b=codename.replace("_","\_")
    codename=b
os.system("bash tg.sh '%s' '%s' '%s' '%s' '%s'"%(device,legv,codename,patch,tgun))
print("\nPosted in Telegram\n")
print("\nExiting...\n")
print("\nBye have a great day\n")
