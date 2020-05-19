import threading, time

threadObj = threading.Thread(target=print, args=['Hello', 'Threading', 'world!'],
                             kwargs={'sep': ' '})
threadObj.start()
