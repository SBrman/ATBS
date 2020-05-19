#! python3

import requests, os, json, sys
import pyinputplus as pyip

omdb_api_key = ''


if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyip.inputStr('TV or Movie name: ')

    
url = 'http://www.omdbapi.com/?apikey=%s&t=%s&plot=full' %(omdb_api_key, search)

res = requests.get(url)
res.raise_for_status()


data = json.loads(res.text)

#path = r''
#os.chdir(path)
os.chdir(r'H:\python\files\omdb Movie or TV show description')

file = open('%s.txt' %(data['Title']), 'w')
for i,key in enumerate(data.keys()):

    if i == 13 or i==14:
        continue
    
    file.write(str(key)+': ' + str(data[key])+'\n')
file.close()


poster_file = open('%s_poster.%s' %(data['Title'],\
                               data['Poster'][ data['Poster'].rfind('.')+1 : ]
                               ), 'wb')
pres = requests.get(data['Poster'])
pres.raise_for_status()

for chunk in pres.iter_content(100000):
    poster_file.write(chunk)
poster_file.close()

print('Done.')
