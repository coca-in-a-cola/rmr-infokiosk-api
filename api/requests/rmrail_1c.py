from tokenize import String
import requests
import xml.etree.ElementTree as ET
from app_secrets import login_1c, password_1c
from config import web_app_1c_host

def get_user_by_card_code(code) -> dict:
    response = requests.post(
        web_app_1c_host + '/ws/request.1cws',
        auth=(login_1c, password_1c),
        data=f"""
        <x:Envelope
            xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:cwe="http://1CWebApp/">
            <x:Header/>
            <x:Body>
                <cwe:ПочучитьСотрудникаПоКоду>
                    <cwe:КодКарты>{code}</cwe:КодКарты>
                </cwe:ПочучитьСотрудникаПоКоду>
            </x:Body>
        </x:Envelope>
        """.encode('UTF-8'),
        headers={'Content-Type': 'application/xml'}
    )
    xml_body = response.text

    parse_fields = {
        'fullname': ('<m:ФИО>', '</m:ФИО>'),
        'personnel_number': ('<m:ТабельныйНомер>', '</m:ТабельныйНомер>'),
        'subdivision': ('<m:Подразделение>', '</m:Подразделение>'),
        'position': ('<m:Должность>', '</m:Должность>'),
        'phone_number': ('<m:НомерТелефона>', '</m:НомерТелефона>'),
    }

    parsed = {}

    for key in parse_fields:
        start, end = parse_fields[key]
        i = xml_body.find(start)
        j = xml_body.find(end)
        if (i != -1 and j != -1):
            parsed[key] = xml_body[i + len(start):j].strip()
    
    return parsed if len(parsed) > 0 else None