<h2 align="center">
  DATA SAMPLING APP
</h2>

## :bulb: About
The module that allows the collection of data sampling, which is transmitted with WebSocket via WIFI or serial port for CSV file.

## :movie_camera: Preview

<div align="center">
  <img src="" />
</div>

## :rocket: Technologies

* [Python3](https://www.python.org/)
* [Pysimplegui](https://pysimplegui.readthedocs.io/en/latest/)

## :raised_hand: Warning
To use this module, remember that data must be transmitted via serial port or WIFI in string where each data has to be separated by a comma.

```json
"00.0000000,00.0000000,00.0000000,00.0000000"
``` 
## :information_source: Getting Started

1. Fork this repository and clone it on your machine.
2. Change the directory to `python-data-sampling-app` where you cloned it.

## :zap: Module Getting Started

1. Install requirements.
```shell
$ pip3 install -r requirements.txt
```
2. Startup
```shell
$ python3 App.py
```
* If you are going to use data transmission via Wifi, when connecting, keep in mind that the WebSocket server `IP` will be your machine's `IP` and port `8080`.
---
Made with :hearts: by Nelson Wenner :wave: [Get in touch!](https://www.linkedin.com/in/nelsonwenner/)