from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os, socket

ip = socket.gethostbyname(socket.gethostname())
PATHFTP = 'D:\FTP'
os.chdir(PATHFTP)

addr = (ip,21)
authorizer = DummyAuthorizer()
authorizer.add_user('Admin','AdminPassword','.', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr,handler)
server.serve_forever()
