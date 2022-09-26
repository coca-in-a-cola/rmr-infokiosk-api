from flask import current_app
import requests

def send(phone, message):
    response = requests.get(current_app.config["GSM_CONNECT_STRING"](phone, message))

    if (response.ok):
        return response
    else:
        raise(Exception(f"GSM failed with response: {response.status} - {response.content}"))