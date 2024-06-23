import socket
import sys
import random
import string

# 定义服务器IP和端口号
#server_ip = '192.168.1.3'
#server_port = 12345
server_ip = input('请输入服务器IP号: ')
server_port = int(input('请输入服务器端口号: '))

Lmin = int(input("最短字节数:"))
Lmax = int(input("最长字节数:"))
N_block = int(input("反转块数:"))

#发送个数
i = 1
# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


Type_BYTES = 2
N_BYTES = 4
Length_BYTES = 4
Data_BYTES = 500
Initialization_FORMAT = "{Type_BYTES}{N_BYTES}"
reverseRequest_FORMAT = "{Type_BYTES}{Length_BYTES}{Data_BYTES}"


# 连接服务器
client_socket.connect((server_ip, server_port))

# 发送Initialization报文
Initialization_message = Initialization_FORMAT.format(Type_BYTES=i,N_BYTES=N_block)
#print(Initialization_message)
client_socket.send(Initialization_message.encode())
# 接收agree报文
response = client_socket.recv(1024).decode()
print("建立完成")


# 发送各个数据块的reverseRequest报文
for j in range(N_block):
    length = random.randint(Lmin, Lmax)
    data = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    #print(data)
    request_message = reverseRequest_FORMAT.format(Type_BYTES=i,Length_BYTES=length,Data_BYTES=data)
    client_socket.send(request_message.encode())
    i += 1
    # 接收服务器返回的reverseAnswer报文
    response = client_socket.recv(1024).decode()
    response = response[2:]
    print(f"第{j+1}块反转的文本: {response}")

# 关闭客户端套接字
client_socket.close()
