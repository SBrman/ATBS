#! python3

'''Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.'''

import requests, bs4, pyperclip, logging, time

#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

address = pyperclip.paste()

res = requests.get(address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

urls = soup.select('a')

for url in urls:
    print('Url-%s: %s' %(urls.index(url)+1 ,url.get('href')))

print('\n\n')

broken_links = []

print('Checking...')
for url in urls:
    
    if str(url.get('href')).startswith('h'):
        url = str(url.get('href'))

    elif str(url.get('href')).startswith(('//','\\\\')):
        url = 'http:'+ str(url.get('href'))

    else:
        url = address + str(url.get('href'))

    logging.debug(url)
    
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        #print('The url: %s' %(url)+ ' does not exist')
        broken_links += [str(url)]
    
    
print('Checking done.\n')

if len(broken_links)==0:
    print('All links are working.')
else:
    print('%s broken links found. The broken links are following:'%(len(broken_links)))
    
    for i in range(len(broken_links)):
        print('%s. %s'%(i+1, broken_links[i]))
