# Imports
import os
from os import path
import time

# Banner
def banner():
    print ("")
    print ("")
    print ("")
    print("""
    ╭╮╭╮╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳━━━╮
    ┃┃┃┃┃┃╱╱┃┃╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱┃╭━╮┃╱╱╱╱╭╮╱╱╱╱╭╯╰╮╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╭━╮┃
    ┃┃┃┃┃┣━━┫┃╭━━┳━━┳╮╭╮╰╮╭╋━━╮┃╰━╯┣━┳━━╋╋━━┳━┻╮╭╯╱┃┃╱╱╭━━┳━━┳┳━━┳━╮┃┃╱┃┃╰━━╮
    ┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃╱┃┃┃╭╮┃┃╭━━┫╭┫╭╮┣┫┃━┫╭━┫┣━━┫┃╱╭┫┃━┫╭╮┣┫╭╮┃╭╮┫┃╱┃┣━━╮┃
    ╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃╱┃╰┫╰╯┃┃┃╱╱┃┃┃╰╯┃┃┃━┫╰━┫╰┳━┫╰━╯┃┃━┫╰╯┃┃╰╯┃┃┃┃╰━╯┃╰━╯┃
    ╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻╯╱╰━┻━━╯╰╯╱╱╰╯╰━━┫┣━━┻━━┻━╯╱╰━━━┻━━┻━╮┣┻━━┻╯╰┻━━━┻━━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱""")
    print ("")
    print ("")
    print ("")
    print ("ONLY FOR OFFICIAL BUILDS/USE")
    print ("")
    print ("")
    print ("")

# OTA
def ota():
    print ("Moving to OTA repository")
    print ("")
    time.sleep(1)
    os.chdir("OTA")
    print("Syncing chnages with our server")
    print ("")
    time.sleep(2)
    print("If this fails with error pls do it manually and fix the freaking conflicts or inform the team")
    print ("")
    print("Unshallowing the repository")
    print ("")
    os.system("git fetch LegionOS-Devices --unshallow")
    os.system("git checkout 11")
    os.system("git pull LegionOS-Devices 11")
    print ("")
    folder=codename
    print ("")
    time.sleep(2)
    print ("Device directory exists:" + str(path.exists(folder)))
    result=path.exists(folder)
    if result==False:
        print("Creating the device folder... xd")
        print ("")
        time.sleep(2)
        os.system("mkdir %s"%folder)
        os.chdir("%s"%folder)
        os.system("mkdir official")
        print("Folder created succesfully... xd")
        print ("")
        time.sleep(2)
        print("Creating the necessary files... xd")
        print ("")
        time.sleep(2)
        os.mknod("changelogs_gapps.txt")
        os.mknod("changelogs_vanilla.txt")
        os.chdir("official")
        os.mknod("gapps.json")
        os.mknod("vanilla.json")
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        print("Creating the necessary files completed succesfully... xd")
        print ("")
        print("Hey new maintainer!!! welcome to the Project LegionOS hope you have a great time here")
    else:
        print("Continuing the script....xd")
        os.system("bash ota.sh %s %s %s %s"%(codename,variant,name,mail))
        print ("")

# Variant selection
def var():    
    if variant==vanilla:
        os.system("export WITH_GAPPS=false")
    else:
        size=input("Enter you size of gapps :- (Full/Minimal)")
        if size==Full:
            os.system("export WITH_GAPPS=true")
            os.system("export TARGET_INCLUDE_STOCK_GAPPS=true")
        else:
            os.system("export WITH_GAPPS=true")

# Upload
def upload():
    sfgu=input("Enter your sourceforge username :- \n")
    print("Logging you into our Sourceforge storage servers\n")
    time.sleep(2)
    print("\nSetps to follow :-\n")
    print("\ncd /home/frs/legionrom/",codename)
    print("\nput filename.zip\n")
    print("\neg:- put /home/legion/out/target/product/legionos.zip\n")
    print("\nAlso remember to press ctrl+z after uploading\n")
    time.sleep(2)
    os.system("sftp %s@frs.sourceforge.net"%sfgu)

# Building
def build():
    os.system(". build/envsetup.sh")
    var()
    os.system("lunch legion_%s-userdebug"%codename)
    os.system("make installclean")
    os.system("make legion")
    upload()
    ota()

# Selection & proceeding further
banner()
print("Select one item from the list below :- \n")
print("1. Build/ship official build with OTA(including uploading) :- \n")
print("2. Upload the Build to sourceforge :- \n")
print("3. Just OTA :- \n")
codename=input("Enter your device code name :- eg miatoll/laurel_sprout : ")
folder=codename
print("")
variant=input("Enter which variant you wanna build :- eg (vanilla/gapps)")
print("")
reply=int(input("Now tell me what you wanna do :- "))
print("")
name=(input("Enter your github name :- "))
print("")
mail=(input("Enter the mail id linked with github :- "))
if reply==1:
    build()
elif reply==2:
    upload()
else:
    ota()    



