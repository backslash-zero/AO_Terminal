import socket
import argparse

# Parse the host and port arguments
parser = argparse.ArgumentParser(description='TCP/IP Server')
parser.add_argument('--host', type=str, dest='host', default='localhost')
parser.add_argument('--port-td', type=int, dest='porttd', default='7654')
parser.add_argument('--port-py', type=int, dest='portpy', default='7655')
parser.add_argument('--debug', type=bool, dest='debug', default=False)
parser.add_argument('--prefix', type=str, dest='prefix', default='➜ ')

args = parser.parse_args()

HOST = args.host  # Set to the IP address of the machine running TouchDesigner
PORT_TD = args.porttd  # Use the same port number as the TouchDesigner TCP/IP DAT
PORT_PY = args.portpy  # Use the same port number as the TouchDesigner TCP/IP DAT
DEBUG = args.debug
PREFIX = args.prefix

# Set the prefix for the input prompt and make it purple
styledPrefix = '\033[95m' + PREFIX + '\033[0m'

# Create a TCP socket
server_socket_td = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_py = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket_td.bind((HOST, PORT_TD))
server_socket_py.bind((HOST, PORT_PY))

# Listen for incoming connections
server_socket_td.listen(1)
if (DEBUG):
    print('Server is listening on {}:{}'.format(HOST, PORT_TD))
server_socket_py.listen(1)
if (DEBUG):
    print('Server is listening on {}:{}'.format(HOST, PORT_PY))

# Accept a connection
client_socket_td, client_address_td = server_socket_td.accept()
if (DEBUG):
    print('Connected to client:', client_address_td)
client_socket_py, client_address_py = server_socket_py.accept()
if (DEBUG):
    print('Connected to client:', client_address_py)

# Receive messages from the client
while True:
    if (DEBUG):
        print('before input')
    data = input(styledPrefix)
    if (DEBUG):
        print('Waiting')
        client_socket_td.sendall('This is the server\n'.encode())
        client_socket_py.sendall('This is the server\n'.encode())
    if data == "exit":
        break
    if (DEBUG):
        print(data)
    client_socket_td.sendall((data + '\n').encode())
    client_socket_py.sendall((data + '\n').encode())


# Close the connection
client_socket_td.close()
server_socket_td.close()
client_socket_py.close()
server_socket_py.close()
