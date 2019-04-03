import os, socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from threading import Thread
from ftplib import FTP

currentData = {}

ftp = FTP('')

def check():
    global currentData
    while 1:
        fileDir = {}

        files = os.listdir()
        for file in files:
            fileDir[file] = file

        if 'new.txt' in fileDir:
            with open(fileDir['new.txt']) as new:
                text = new.readlines()
            if not text:
                pass
            else:
                text = [i.strip() for i in text]
                currentData[text[0]] = list(text[1:len(text)])
                os.remove('new.txt')
                continue
        elif 'findme.txt' in fileDir:
            with open(fileDir['findme.txt.']) as new:
                found = new.readlines()
            if not found:
                pass
            else:
                for ip, filename in currentData.items():
                    files = ''.join(filename)
                    if found[0] in files:
                        print(ip)
                    else:
                        print('Could not find file')
                    os.remove('findme.txt')
                    continue

# Starts the server
def main():
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous('.', perm='elradfmwM')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner= "Connected"

    server = ThreadedFTPServer(('127.0.0.1', 1026), handler)
    server.serve_forever()


if __name__ == "__main__":
    thread = Thread(target = check())
    thread.start()
    main()
    thread.join()
