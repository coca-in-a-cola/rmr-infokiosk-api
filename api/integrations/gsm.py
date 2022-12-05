from flask import current_app
import json
import urllib.parse
import requests
import asyncio
from threading import Thread
import copy

app_config_crutch = None

def send(phonenumber, message, attempts = 10, delay_seconds = 0.5):

    #Костыль 1
    global app_config_crutch
    if not app_config_crutch:
        app_config_crutch = copy.deepcopy(current_app.config)

    #Костыль 2
    thread = Thread(target=start_thread,
        kwargs=dict(phonenumber=phonenumber, message=message, attempts=attempts, delay_seconds=delay_seconds))
    thread.start()
    return


def start_thread(**kwargs):
    #Костыль 3
    asyncio.run(send_async(**kwargs))

async def send_async(phonenumber, message, attempts = 5, delay_seconds = 0.5):
    for idx in range(attempts):
        r = await __send_attempt(phonenumber, message)
        print(f"GSM attempt {idx + 1}")
        if (r):
            print("GSM success!")
            return r
        else:
            print(f"GSM Fail.")
            if idx != attempts - 1:
                print(f"Repeating in {delay_seconds}s...")
            await asyncio.sleep(delay_seconds)

    return False


async def __send_attempt(phonenumber, message):
    params = dict(phonenumber=phonenumber, message=message)
    params.update(app_config_crutch["GSM_PARAMS"])
    response = requests.get(
        app_config_crutch["GSM_CONNECT_STRING"],
        params=params,
        headers=app_config_crutch["GSM_HEADERS"],
        proxies=dict(http=app_config_crutch['PROXY_SERVER']),
        verify=False)
        
    return is_success(response)


def is_success(response):
    if not response.ok:
        return False
    
    try:
        json = response.json()
        return json['report'][0]['1'][0]['result'] == 'success'
    except:
        return False