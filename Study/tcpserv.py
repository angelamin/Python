import socket

HOST=''
PORT=3214
# 没有参数时 默认为tcp协议
s=soket.soket();
s.bind((HOST,PORT))

s.listen(5)
# 客户端连接对象及连接地址
clnt,addr=s.accept()
print('Client Address:',addr)

while True:
	data=clnt.recv(1024)
	if not data:
		break
	print('receive data:',data.decode('utf-8'))
	# 将数据返回给客户端
	clnt.send(data)

clnt.close()
s.close()
