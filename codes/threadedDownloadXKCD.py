#! python3

'''Need to FIX not all files were downloaded.

threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.'''

import requests, bs4, threading, os

os.chdir(r'H:\python\files\Chapter 17')
os.makedirs('.\\XKCD comics', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        #Download the page
        print('Downloading page https://xkcd.com/%s...\n' %(urlNumber))
        res = requests.get('https://xkcd.com/%s' %(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        #Find url of the comic image
        comicElem = soup.select('#comic img')

        # Getting number of the Comic 
        elem = soup.select('#middleContainer.box ul.comicNav li a')
        comicNumber = elem[1].get('href').replace('/','')
        
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            #Download image
            print('Downloading image %s...' %(os.path.basename(comicUrl)))
            res = requests.get('https:'+ comicUrl)
            res.raise_for_status()

            #Save img to XKXD comics
            imageFile = open(os.path.join('.\\XKCD comics','%s. %s'\
                               %(comicNumber, os.path.basename(comicUrl))), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

            imageFile.close()


# Total Comics number
resT = requests.get('https://xkcd.com')
resT.raise_for_status()
soupT = bs4.BeautifulSoup(resT.text, 'html.parser')
# Getting number of the Comic 
elemT = soupT.select('#middleContainer.box ul.comicNav li a')
comicNumberT = elemT[1].get('href').replace('/','')
lastComicNumber = int(comicNumberT)


# Create the thread objects
downloadThreads = []

for i in range(0, lastComicNumber, 100):
    start = i
    end = i+99

    if start == 0:
        start = 1

    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
