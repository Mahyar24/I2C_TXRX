#! /usr/bin/python3.7

"""
Mahyar@Mahyar24.com, Sat 08 Jan 2022.
"""

import socket
import threading
import time

INTERFACE = "eth0"  # REPLACE IT WITCH DESIRED INTERFACE!
PORT = 1234  # REPLACE IT WITCH ACTUAL PORT NUMBER!

INTERVAL = 1

RX_FILE = f"/sys/class/net/{INTERFACE}/statistics/rx_bytes"
TX_FILE = f"/sys/class/net/{INTERFACE}/statistics/tx_bytes"

PASSWORD = b"<PASSWORD>"  # Adding some funny security barrier!

ADDR = tuple()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(None)
sock.bind(("", PORT))


def hr_size(size_b, interval, k=1000, accuracy=2):
    units = ("B/S", "KB/S", "MB/S", "GB/S", "TB/S")
    speed = size_b / interval
    pattern = "{:6.{}f}{:5}"
    for i, unit in enumerate(units[:-1]):
        x = speed / (k ** i)
        if x < k:
            return pattern.format(x, accuracy, unit)
    return pattern.format(speed / (k ** (len(units) - 1)), accuracy, units[-1])


def get_rx():
    with open(RX_FILE) as rx_file:
        while True:
            yield int(rx_file.readline())
            rx_file.seek(0)


def get_tx():
    with open(TX_FILE) as rx_file:
        while True:
            yield int(rx_file.readline())
            rx_file.seek(0)


def populate_msg():
    begin = True
    for r, t in zip(get_rx(), get_tx()):
        if not begin:
            yield bytes(
                f"RX:  {hr_size(r - previous_r, INTERVAL)},"
                f"TX:  {hr_size(t - previous_t, INTERVAL)}",
                "UTF-8",
            )
        else:
            begin = False

        previous_r, previous_t = r, t


def listen():
    global ADDR

    while True:
        msg, address = sock.recvfrom(1024)
        if msg == PASSWORD:
            # print(address)
            ADDR = address


def send():
    for msg in populate_msg():
        # print(f"send -> {ADDR}")
        if ADDR:
            try:
                sock.sendto(msg, ADDR)
            except OSError:
                pass
        time.sleep(1)


def main():
    listen_thread = threading.Thread(target=listen, daemon=True)
    listen_thread.start()

    send()


if __name__ == "__main__":
    main()
