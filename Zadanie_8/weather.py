import os
import sys
import datetime
import requests
import json


class HistoryHendler:
    def __init__(self):
        self.__filepath = 'history.json'
        self.__history = {}

    def check_date(self, date):
        date = str(date)
        precip = [True, self.__history.get(date)] if date in self.__history.keys() else [False]
        return precip

    def load_history(self, days):
        if os.path.exists(self.__filepath):
            with open(self.__filepath, 'r') as file:
                self.__history = json.load(file)
            return self.check_date(days)
        else:
            return [False]

    def get_history(self):
        return self.__history

    def save_history(self, date, precip):
        self.__history[str(date)] = precip
        with open(self.__filepath, 'w') as file:
            json.dump(self.__history, file)


class WeatherForcast:
    def __init__(self, key):
        self.__KEY = key
        self.API_URL_h = "https://visual-crossing-weather.p.rapidapi.com/history"
        self.API_URL_f = "https://visual-crossing-weather.p.rapidapi.com/forecast"
        self.querystring = {}
        self.__history = HistoryHendler()
        self.__headers = {
            'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
            'x-rapidapi-key': self.__KEY
        }

    def items(self):
        for key, element in self.__history.get_history().items():
            element = "Będzie padać " if float(element) > 0.0 else "Nie będzie padać"
            yield tuple([key,element])

    def __getitem__(self, date):
        precipitation = self.__history.load_history(date)
        if not precipitation[0]:
            url = self.API_URL_h if date < datetime.date.today() else self.API_URL_f
            day_format = str(date) + 'T00:00:00'
            self.querystring = {
                "startDateTime": day_format,
                "aggregateHours": "24",
                "location": "Sanok, PL",
                "endDateTime": day_format,
                "unitGroup": "metric",
                "contentType": "json",
                "shortColumnNames": "true"
            }
            response = requests.request("GET", url, headers=self.__headers, params=self.querystring)
            if 'locations' in response.json().keys():
                collections = response.json()["locations"].get(self.querystring['location']).get("values")
                for values in collections:
                    if values.get('datetimeStr')[0:10] == str(date):
                        precipitation = [True, values.get('precip')]
                        self.__history.save_history(date, precipitation[1])
                        break
        print("Nie Wiem" if not precipitation[0] else "Będzie padać" if float(precipitation[1]) > 0.0
                else "Nie będzie padać")

    def __iter__(self):
        return iter(self.__history.get_history().keys())


key = sys.argv[1] if len(sys.argv) > 1 else ""
today = datetime.date.today()
try:
    day = datetime.datetime.strptime(sys.argv[2], '%d-%m-%Y').date()
except IndexError:
    day = today + datetime.timedelta(days=1)

wf = WeatherForcast(key)
print("wf[data]")
wf[day]debilek3
print()
print("wf.items()")
for cos in wf.items():
    print(cos)
print()
print("wf")
for element in wf:
    print(element)
