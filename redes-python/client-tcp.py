import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4466))
client.send(b"a\n")
pkg = client.recv(1024).decode()
print(pkg)