import socket

HOST='127.0.0.1'
PORT='3214'

s=socket.socket()

try:
	s.connect((HOST,PORT))
	data='你好'
	while data:
		s.sendall(data.encode('utf-8'))
		data=recv(1024)
		print('receive from server:',data.decode('utf-8'))
		data=input('please input an info:\n')
except socket.error as error:
	print(error)
finally:
	s.close()