from datetime import date

sequenceNumber = 0
lastDate = None

def du_task_number():
    d = date.today().strftime("%m%d%y")
    global lastDate, sequenceNumber
    if (d != lastDate):
        sequenceNumber = 0
        lastDate = d

    sequenceNumber += 1

    return f"{str(sequenceNumber).zfill(4)}{lastDate.zfill(6)}"
