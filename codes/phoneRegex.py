#! python3
import re

phoneRegex = re.compile(r'''(                         
                        (\d{3}|\(\d{3}\))?          # area code
                        (\s|-|\.)?                  # separator
                        \d{3}                       # first 3 digits
                        (\s|-|\.)                   # separator
                        \d{4}                       # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
                        )''', re.VERBOSE)

text = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo = phoneRegex.findall(text)
print(mo)
for i in range(len(mo)):
    print('Number-' + str(i+1) +': '+ mo[i][0])
    
