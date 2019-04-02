import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
from threading import Thread

currentData = {}

def check():
    global currentData
    while 1:
        fileDir = {}

        files = os.listdir()
        for file in files:
            fileDir[file] = file

        if 'new.txt' in fileDir:
            with open(fileDir['new.txt']) as new
                text = new.readlines()
            if not text:
                pass
            else:
                text = [i.strip() for i in text]
                currentData[text[0]] = list(text[1:len(text)])
                os.remove('new.txt')
                continue

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "pass", ".", perm="elradfmw")
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner= "Connected"

    server = FTPServer(("127.0.0.1", 3001), handler)
    server.serve_forever()


if __name__ == "__main__":
    thread = Thread(target = check())
    thread.start()
    main()
    thread.join()
