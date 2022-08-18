from os import system, mkdir, popen,remove
try:from urllib.request import urlopen
except ImportError:system("pip install urllib");from urllib.request import urlopen
from shutil import rmtree
from time import sleep
from zipfile import ZipFile
options_list='''(1) Install krnl beta
(2) unintall krnl beta
(3) install requirements
(4) fix vpn issue
(5) exit'''
def ping(host):return len(popen("ping -n 1 "+host).read().split("\n"))!=2
def get_exact_path(old_path):return popen("echo " + old_path).read()
def show_options(error=""):
    system("clear")
    print(options_list+error)
    run_option(input("~ "))
def run_option(option=False):
    try:
        int(option)
        option_is_integer=True
    except:
        option_is_integer=False
    if option_is_integer and int(option) in range(1,5):
        option=int(option)
        if option==1:
            install_krnl_beta()
        elif option==3:
            install_requirements()
        if option==5:
            exit()
    else:
        show_options("\nINVALID OPTION SELECTED, please try again")
def download(url, path):
    filedata = urlopen(url)
    datatowrite = filedata.read()
    with open(path, 'wb') as f:
        f.write(datatowrite)
def install_krnl_beta():
    if ping("k-storage.com"):
        print("You dont really need to use this way to install the beta, just use krnl_beta.exe from krnl.place\nI'll download and run it anyways for you!")
        download("https://k-storage.com/krnl_beta.exe", "krnl_beta.exe")
    elif ping("https://benomat3000.web.app/"):
        print("Seems like you can't reach k-storage.com. We will use a different source for the download to fix this.")
        krnldir=get_exact_path('%appdata%\\Krnl\\')
        mkdir(krnldir)
        download("https://benomat3000.web.app/krnldownloads/krnlbeta.zip",krnldir+"download.zip")
        ZipFile.extractall(krnldir+"download.zip")
        remove(krnldir+"download.zip")
        print("Successfully downloaded!");sleep(5);show_options()
    else: print("Seems like you can't reach k-storage.com or my download. Please use the zip from pins in #user-help. Press Enter to return to the options"); input(); show_options()
def install_requirements():
    mkdir("temp")
    print("Downloading installers")
    download("https://aka.ms/vs/16/release/vc_redist.x64.exe", "temp\\vc_redist.x64.exe")
    download("https://aka.ms/vs/16/release/vc_redist.x86.exe", "temp\\vc_redist.x86.exe")
    download("https://go.microsoft.com/fwlink/?LinkId=2085155", "temp\\dotnet4.8-runtime.exe")
    print("Please Go through the steps of these installers!!")
    print("startings vc_redist.x64.exe")
    system("vc_redist.x64.exe")
    print("starting vc_redist.x86.exe")
    system("vc_redist.x86.exe")
    print("starting dotnet4.8-runtime.exe")
    system("dotnet4.8-runtime.exe")
    print("deleting installers")
    rmtree('temp')
    sleep(1)
    show_options()
show_options()
