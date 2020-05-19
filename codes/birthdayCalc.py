#! python3

'''birthdayCalc.py **(This is not totally accurate)
USAGE --
birthdayCalc year month day(optional) hour(optional) minute(optional) second(optional)'''

import datetime, sys

birthday = {'year':0,'month':0,'day':0,'hour':0,'minute':0,'second':0}

if len(sys.argv) <2:
    for key in birthday.keys():
        birthday[key] = input(key+': ')
        if birthday[key] == '':
            birthday[key] = 0
        else:
            birthday[key] = int(birthday[key])

elif len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        birthday[list(birthday.keys())[i-1]] = int(sys.argv[i])
else:
    print('USAGE - birthdayCalc year month day(optional) hour(optional) minute(optional) second(optional)')
    sys.exit()

birth = datetime.datetime(birthday['year'],birthday['month'],birthday['day'],\
                          birthday['hour'],birthday['minute'],birthday['second'])


time = datetime.datetime.now() - birth

age_plus_2000_1_1 = datetime.datetime(2000,1,1)+time
age_year = age_plus_2000_1_1.year - 2000
age_month = age_plus_2000_1_1.month - 1
age_day = age_plus_2000_1_1.day - 1
age_hour = age_plus_2000_1_1.hour
age_minute = age_plus_2000_1_1.minute
age_second = age_plus_2000_1_1.second

print('%s years, %s months, %s days, %s hours, %s miuntes and %s seconds old.'
      %(age_year, age_month, age_day, age_hour, age_minute, age_second))
