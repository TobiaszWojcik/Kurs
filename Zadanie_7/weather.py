import os
import sys
import datetime
import requests
import json


class HistoryHendler:
    def __init__(self):
        self.filepath = 'history.json'
        self.history = {}

    def check_date(self, date):
        date = str(date)
        precip = [True, self.history.get(date)] if date in self.history.keys() else False
        return precip

    def load_history(self, days):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                self.history = json.load(file)
            return self.check_date(days)
        else:
            return False

    def save_history(self, date, precip):
        self.history[str(date)] = precip
        with open(self.filepath, 'w') as file:
            json.dump(self.history, file)


today = datetime.date.today()
day = datetime.datetime.strptime(sys.argv[2], '%d-%m-%Y').date() if len(sys.argv) > 2 \
    else today + datetime.timedelta(days=1)


history = HistoryHendler()
if precipitation := history.load_history(day):
    pass
else:
    API_URL_h = "https://visual-crossing-weather.p.rapidapi.com/history"
    API_URL_f = "https://visual-crossing-weather.p.rapidapi.com/forecast"
    url = API_URL_h if day < today else API_URL_f
    key = sys.argv[1] if len(sys.argv) > 1 else ""
    day_format = str(day)+'T00:00:00'
    querystring = {
        "startDateTime": day_format,
        "aggregateHours": "24",
        "location": "Sanok, PL",
        "endDateTime": day_format,
        "unitGroup": "metric",
        "contentType": "json",
        "shortColumnNames": "true"
    }
    headers = {
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
        'x-rapidapi-key': key
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    collections = []

    if 'locations' in response.json().keys():
        collections = response.json()["locations"].get("Sanok, PL").get("values")
        for values in collections:
            if values.get('datetimeStr')[0:10] == str(day):
                precipitation = [True, values.get('precip')]
                history.save_history(day, precipitation[1])
                break
            precipitation = [False]
    else:
        precipitation = [False]

# W przypadku pogody na przyszłość api pobiera 15 dni w przód i trzeba odfiltrować odpowiedni dzień

if precipitation[0]:
    print("Będzie padać" if float(precipitation[1]) > 0.0 else "Nie będzie padać")
else:
    print("Nie wiem")
