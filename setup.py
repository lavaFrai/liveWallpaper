import os
from elevate import elevate
import shutil
import sys
import winreg

from termcolor import colored
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def error(text):
    print(colored("[ERROR]\t" + text, "red"))
    input("[Press enter to exit]")
    exit(1)


def info(text):
    print(colored("[INFO]\t" + text, "white"))


def warn(text):
    print(colored("[WARN]\t" + text, "yellow"))


def ask(text):
    print(colored("[ASK]\t" + text, "blue"))
    tmp = ""
    while tmp not in ['y', 'n', 'д', 'н']:
        print(colored("(type '", "blue") + colored("y", "green") + colored("' or '", "blue") + colored("n",
                                                                                                       "green") + colored(
            "' and press enter) ?>", "blue"), end='')
        tmp = input().lower()
    return tmp in ['y', 'д']


def setup(path):
    info("Creating a folder in program files C:\\Program Files\\lava_frai\\liveWallpaper\\")
    elevate(show_console=False)
    if os.path.exists("C:\\Program Files\\lava_frai\\liveWallpaper\\"):
        shutil.rmtree("C:\\Program Files\\lava_frai\\liveWallpaper\\")
    os.makedirs("C:\\Program Files\\lava_frai\\liveWallpaper\\")
    for i in os.listdir("C:\\Program Files\\lava_frai\\liveWallpaper\\"):
        os.remove("C:\\Program Files\\lava_frai\\liveWallpaper\\" + i)
    for i in ["main.py", "color.py", "wallpaper.py"]:
        info("Copying file " + i)
        shutil.copy(path + i, "C:\\Program Files\\lava_frai\\liveWallpaper\\" + i)
    for i in ["forms", "resources"]:
        shutil.copytree(path + i, "C:\\Program Files\\lava_frai\\liveWallpaper\\" + i)
        info("Copying catalog " + i)
    info("Adding entries to the registry")
    regEntrie = '"' + sys.executable[:sys.executable.rindex(
        '\\') + 1] + 'pythonw.exe" "C:\\Program Files\\lava_frai\\liveWallpaper\\main.py"'
    key = winreg.OpenKey(
        key=winreg.HKEY_CURRENT_USER,
        sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
        reserved=0,
        access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'liveWallpaper', None, winreg.REG_SZ, regEntrie)
    winreg.CloseKey(key)
    # print(regEntrie)
    if ask("To continue, you need to restart your computer. Do it now?"):
        os.system("shutdown -r -t 0")
    else:
        info("Installation finished, please, reboot PC")
        input("[Press enter to finish]")


if not ctypes.windll.shell32.IsUserAnAdmin():
    error("You need to run as an administrator")
info("Starting liveWallpaper installing...")
info("Checking operating system")
if os.name != "nt":
    error("Sorry, supported only Windows NT system")
path = os.path.abspath(__file__)
path = path[:path.rindex('\\') + 1]
info(f"Running in directory {path}")
if not ask("The liveWallpaper program will be installed on your computer and added to autorun. You agree?"):
    error("The user refused to install")
try:
    setup(path)
except BaseException as e:
    error("Unexpected error: " + str(e))
