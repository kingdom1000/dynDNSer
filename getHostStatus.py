import requests
import socket

def internalIP():
    return socket.gethostbyname(socket.gethostname())

def externalIP():
    getIp = requests.request('GET', 'http://myip.dnsomatic.com')
    ip = getIp.text
    return ip

