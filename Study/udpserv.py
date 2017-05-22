import socket
HOST=''
PORT=3214
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
# 初始化data
data=True

while Data:
	data,addr=s.recvfrom(1024)
	if Data == b'bye':
		break;
	print('receive string:',data.decode('utf-8'))
	s.sendto(data,addr)

s.close()

