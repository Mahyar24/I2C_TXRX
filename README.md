# I2C-TXRX
Run this code for displaying your server TX-RX on a 16*2 I2C display with the help of a RPi!

## Server-Side Installation and Running

Use the [git](https://git-scm.com/downloads) to clone this repository.

```bash
git clone https://github.com/Mahyar24/I2C_TXRX && cd I2C_TXRX;
```
now, **FILL THE PLACEHOLDERS IN THE `server.py:11:0`, `server.py:12:0` and `server.py:19:0` FILES FOR CUSTOMIZING YOUR INTERFACE NAME, PORT AND PASSWORD!****

For starting the program:
```bash
python3.7 server.py
```

## Client-Side Installation and Running

First, you must install [this driver](https://github.com/the-raspberry-pi-guy/lcd). Then, use the [git](https://git-scm.com/downloads) to clone this repository.

```bash
git clone https://github.com/Mahyar24/I2C_TXRX && cd I2C_TXRX;
```
now, **FILL THE PLACEHOLDERS IN THE `client.py:16:0`, `client.py:17:0` FILES FOR CUSTOMIZING YOUR IP, PORT AND PASSWORD!****

For starting the program:
```bash
python3.7 client.py
```

P.S: Compatible with python3.7+.


## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change for significant changes.

Contact me: <OSS@Mahyar24.com> :)

## License
[GNU GPLv3 ](https://choosealicense.com/licenses/gpl-3.0/)
