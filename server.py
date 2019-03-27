from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "pass", ".", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer
handler.banner= "Connected"

server = FTPServer(("127.0.0.1", 3000), handler)
server.serve_forever()
