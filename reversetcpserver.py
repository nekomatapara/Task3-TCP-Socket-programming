import socket
import sys

# 定义服务器IP和端口号
server_ip = '0.0.0.0'  # 监听所有可用的网络接口
server_port = 12345
#server_port = int(input('请输入服务器端口号: '))

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口号
server_socket.bind((server_ip, server_port))

# 监听连接
server_socket.listen(1)

#发送个数
i = 1

print("服务器已启动，等待客户端连接...")


Type_BYTES = 2
N_BYTES = 4
Length_BYTES = 4
Data_BYTES = 500
Agree_FORMAT = "{Type_BYTES}"
reverseAnswer_FORMAT = "{Type_BYTES}{Length_BYTES}{Data_BYTES}"

# 接受客户端连接
client_socket, client_address = server_socket.accept()

print("客户端已连接:", client_address)

# 接收Initialization报文
init_message = client_socket.recv(1024).decode()
N = int(init_message[1:])
# 发送agree报文
Agree_message = Agree_FORMAT.format(Type_BYTES=bin(i))
client_socket.send(Agree_message.encode())
print("建立完成")



# 处理各个数据块的reverseRequest报文
for j in range(N):
    request_message = client_socket.recv(1024).decode()
    length = request_message[1:2]
    data = request_message[2:]
    print(data)
    # 反转数据块
    reverse_data = data[::-1]

    # 发送reverseAnswer报文
    response_message = reverseAnswer_FORMAT.format(Type_BYTES=i+1,Length_BYTES=length,Data_BYTES=reverse_data)
    client_socket.send(response_message.encode())
    i += 1

# 关闭服务器套接字
server_socket.close()