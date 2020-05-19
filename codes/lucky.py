#! python3

'''lucky.py - Opens several Google search results.
Usage: google tabNumbers keywords'''

import sys, os, requests, webbrowser, bs4

google = 'https://www.google.com/'


if len(sys.argv) > 2:
    search = ''.join(sys.argv[2:])
    tabNumbers = sys.argv[1]

elif len(sys.argv) == 1:
    search = input('Enter what to search: ')
    tabNumbers = input('How many tabs to open (at most): ')

elif len(sys.argv) == 2:
    search = ''.join(sys.argv[1])
    tabNumbers = 10

    
address = google + 'search?q=' + search
webbrowser.open(address)

print('Googling...')
res = requests.get(address)
res.raise_for_status()


pages = bs4.BeautifulSoup(res.text, features = "html.parser")
urls = pages.select('div#main > div > div > div > a')

tabs = min(int(tabNumbers), len(urls))
print(str(tabs) + ' results found on the first page.')

for i in range(tabs):
    webbrowser.open(google + urls[i].get('href'))
