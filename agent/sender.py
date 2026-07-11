import requests

SERVER = "http://127.0.0.1:8000/event"

def send(event):
    try:
        requests.post(SERVER, json=event)
    except:
        pass
