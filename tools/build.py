# Imports
import os
from os import path

# Banner
print ("")
print ("")
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
print ("")
print ("")
print ("ONLY FOR OFFICIAL BUILDS/USE")
print ("")
print ("")
print ("")

# Variables
os.system(". build/envsetup.sh")
codename=input("\nEnter your device code name :- eg miatoll/laurel_sprout : \n")
variant=input("\nEnter which variant you wanna build :- eg (vanilla/gapps): \n")
name=(input("\nEnter your github name :- \n"))
mail=(input("\nEnter the mail id linked with github :- \n"))

# Variant
if variant==gapps:
    size=input("\nEnter you size of gapps :- (Full/Minimal)\n")
    if size==Full:
        os.system("export WITH_GAPPS=true")
        os.system("export TARGET_INCLUDE_STOCK_GAPPS=true")
    else:
        os.system("export WITH_GAPPS=true")

# BUilding
os.system("lunch legion_%s-userdebug"%codename)
os.system("make installclean")
os.system("make legion")

# Uploading
sfun=input("\nEnter your sourceforge username :- \n")
print("\nLogging you into our Sourceforge storage servers\n")
print("\nRemember to press ctrl+z after uploading\n")
os.system("sftp %s@frs.sourceforge.net"%sfun)

# OTA
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
    os.chdir("%s"%codeame)
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
else:
    print("\nContinuing the script....xd\n")
    os.system("bash ota.sh %s %s %s %s"%(codename,variant,name,mail))
    print ("")

# Telegram notification
print("\nPosting in Telegram....\n")
os.system("bash tg.sh")
print("\nPosted in Telegram\n")
print("\nExiting...\n")
print("\nBye have a great day\n")
