import socket


# 服务器主机和端口

host = ''
port = 2000

# 新建 socket
# bind 绑定服务器的 host 和 port
s = socket.socket()
s.bind((host, port))

def read_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

# 接受请求
while True:
    # 用 listen 监听请求
    s.listen(5)
    connection, address = s.accept()

    # 用 recv 接收客户端发送的请求数据
    request = connection.recv(1024)

    request = request.decode('utf-8')
    if len(request) == 0:
        continue

    line = request.split('\n')[0]
    print(line)
    path = line.split()[1]
    print(path)

    normal_response = b'Hello World!'
    img_response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello img!<img src="img/img.gif">'
    if path == '/':
        r = normal_response
    elif path == '/img':
        r = img_response
    else:
        r = b'404 NOT FOUND'

    # 用 sendall 把响应数据发送给客户端
    connection.sendall(r)

    # 用 close 关闭连接
    connection.close()
