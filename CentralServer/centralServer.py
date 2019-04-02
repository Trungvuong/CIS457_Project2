import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()
authorizer.add_user("user", "pass", ".", perm="elradfmw")
authorizer.add_anonymous(os.getcwd())

handler = FTPHandler
handler.authorizer = authorizer
handler.banner= "Connected"

server = FTPServer(("127.0.0.1", 3001), handler)
server.serve_forever()
