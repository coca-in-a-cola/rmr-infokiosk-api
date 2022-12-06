from datetime import date
from definitions import basedir
import os
import json

sequenceNumber = 0
lastDate = None

try:
    read_number = open(os.path.join(basedir, "du_sequence.json"), 'r')
    sequenceNumber, lastDate = json.load(read_number)
    read_number.close()
except:
    sequenceNumber = 0
    lastDate = None


def du_task_number():
    d = date.today().strftime("%d%m%y")
    global lastDate, sequenceNumber
    if (d != lastDate):
        sequenceNumber = 0
        lastDate = d

    sequenceNumber += 1

    save_number = open(os.path.join(basedir, "du_sequence.json"), 'w')
    save_number.write(json.dumps([sequenceNumber, lastDate]))
    save_number.close()

    return f"{str(sequenceNumber).zfill(4)}{lastDate.zfill(6)}"
