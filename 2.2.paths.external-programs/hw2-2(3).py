import os
import subprocess


if __name__ == "__main__":
    path = os.path.normpath('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
    code = subprocess.check_call([path, 'ya.ru'])
