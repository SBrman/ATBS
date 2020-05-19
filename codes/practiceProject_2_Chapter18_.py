#! python3

import requests, json, sys, datetime, time
import pyinputplus as pyip

APPID = ''

if len(sys.argv) == 1:
    city = pyip.inputStr('Enter city name in bangladesh: ')
    location = city + ', BD'
else:    
    if len(sys.argv)<3:
        print('USAGE -- getOpenWeather city_name, 2-letter_country_code')
        sys.exit()
        location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&units=metric&APPID=%s'\
      %(location, APPID)

res = requests.get(url)
res.raise_for_status()

data = json.loads(res.text)

weather = {'sunrise': (data['city']['sunrise']),
           'sunset': data['city']['sunset'],
           'des': {}}

for listInTime in data['list']:
    weather['des'].setdefault(listInTime['dt'],listInTime['weather'][0]['description'])

msg = ''
for key, value in weather.items():
    if type(value) is dict:
        for k,v in value.items():
            msg += (datetime.datetime.fromtimestamp(k).strftime(\
                                        '%I:%M:%S %p [%B %d, %Y]')+': '+str(v)+'\n')
    else:
        msg += (str(key)+': '+datetime.datetime.fromtimestamp(value).strftime(\
                                                    '%I:%M:%S %p [%B %d, %Y]')+'\n')
sys.path.append(r'H:\python\codes')
import textMe
text_report = textMe.textMe(msg)
print('Text SID: %s\nText Status: %s\nText sent at %s\n'
      %(text_report[0], text_report[1], text_report[2]))
