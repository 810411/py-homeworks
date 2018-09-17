import os
import subprocess


if __name__ == "__main__":
    path = os.path.normpath('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
    code = subprocess.call([path, 'ya.ru'])
    if code == 0:
        print("Well done!")
    else:
        print("Something went wrong!")
