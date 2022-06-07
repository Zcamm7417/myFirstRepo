try:
    import requests
    from datetime import date
    import time
    from plyer import notification
except ModuleNotFoundError:
    print('Modules not found, please run pip install -r requirment.txt to install the require modules.')
    exit()
if data != None:
    text = data.json()

while True:
    dateOfStarting = text['dateOfStarting']
    numberOfExam = text['numberOfExam']
    numberOf4Units = text['numberOf4Units']
    dateOfEnd = text['dateOfEnd']

    nofication.notify(
        title = f'Examination notifier on {date.today()}',
        message = f'Exam starts on: {dateOfStarting}\n Number of Exams: {numberOfExam}\n Number of 4 units coureses: {numberOf4Units}\n End of Exam: {dateOfEnd}',
        timeout = 45
    )
    time.sleep(60*60*2)