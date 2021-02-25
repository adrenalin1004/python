import socket
import sys

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('소캣 생성')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind Error! : ' + str(msg[0]) + 'Message' + msg[1])
    sys.exit()
print('Socket bind 성공 !')

s.listen(10)
print('socket listen')

while 1:
    conn, addr = s.accept()
    print('연결!'+addr[0]+':'+str(addr[1]))
s.close()