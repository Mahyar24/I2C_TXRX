#! /usr/bin/python3.7

"""
Mahyar@Mahyar24.com, Sat 08 Jan 2022.
"""

import socket
import threading
import time
from itertools import cycle

import drivers

LCD = drivers.Lcd()

SERVER = ("1.1.1.1", 1234)  # REPLACE IT WITCH ACTUAL PORT NUMBER!
PASSWORD = b"<PASSWORD>"  # Adding some funny security barrier!


TIMEOUT_SEC = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT_SEC)


def send():
    while True:
        if not connected.is_set():
            print("sending")
            try:
                sock.sendto(PASSWORD, SERVER)
            except OSError:  # In case of unreachable network.
                pass
        time.sleep(TIMEOUT_SEC)


def listen():
    msg_cycle = cycle(
        (b"Connection Lost!, Try to Connect ", b"Connection Lost!,!Try to Connect!")
    )
    while True:
        try:
            data = sock.recv(1024)
            connected.set()
            yield data
        except socket.timeout:
            connected.clear()
            yield next(msg_cycle)


def display_msg():
    for msg in listen():
        line1, line2 = msg.decode("utf-8").split(",")
        LCD.lcd_display_string(line1, 1)
        LCD.lcd_display_string(line2, 2)


def main():
    send_thread = threading.Thread(target=send, daemon=True)
    send_thread.start()
    display_msg()


if __name__ == "__main__":
    LCD.lcd_clear()
    connected = threading.Event()
    main()
