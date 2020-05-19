#! python3

import re, pyperclip

text = pyperclip.paste()

def siteFinder():
    siteRegex = re.compile(r'''(
                                (http
                                s?
                                ://
                                \.?)?
                                (www\.)?
                                (\S+?)
                                \.
                                \w{2,5}
                                )''',re.VERBOSE|re.IGNORECASE)
    
    mo = siteRegex.findall(text)
    return mo

siteList = siteFinder()

for i in range(len(siteList)):
    print(siteList[i][0])
