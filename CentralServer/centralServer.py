'''
This is the Central Server that tracks current users 
and files sent to site.

@author Trung-Vuong Pham, Ryan Eisenbarth, and Kevin Holkeboer
@version 1.0
@date April 3, 2019
'''

import os
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer


def main():
    # Authorizes the users in the server
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "pass", ".", perm="elradfmw")
    authorizer.add_anonymous('.', perm='elradfmwM')
    
    # Request handlers
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner= "Connected"
    
    pipe = os.popen("ip -4 route show default").read().split()
    sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sckt.connect((pipe[3], 0))
    address = sckt.getsockname()[0]

    # Creates server in port 3001
    server = ThreadedFTPServer((address, 3001), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
