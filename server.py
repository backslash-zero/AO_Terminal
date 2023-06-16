import socket
import argparse

# Parse the host and port arguments
parser = argparse.ArgumentParser(description='TCP/IP Server')
parser.add_argument('--host', type=str, dest='host', default='localhost')
parser.add_argument('--port', type=int, dest='port', default='7654')
parser.add_argument('--debug', type=bool, dest='debug', default=False)
parser.add_argument('--prefix', type=str, dest='prefix', default='➜ ')

args = parser.parse_args()

HOST = args.host  # Set to the IP address of the machine running TouchDesigner
PORT = args.port  # Use the same port number as the TouchDesigner TCP/IP DAT
DEBUG = args.debug
PREFIX = args.prefix

# Set the prefix for the input prompt and make it purple
styledPrefix = '\033[95m' + PREFIX + '\033[0m'

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

if (DEBUG):
    print('Server is listening on {}:{}'.format(HOST, PORT))

# Accept a connection
client_socket, client_address = server_socket.accept()
if (DEBUG):
    print('Connected to client:', client_address)

# Receive messages from the client
while True:
    if (DEBUG):
        print('before input')
    data = input(styledPrefix)
    if (DEBUG):
        print('Waiting')
        client_socket.sendall('This is the server\n'.encode())
    if data == "exit":
        break
    if (DEBUG):
        print(data)
    client_socket.sendall((data + '\n').encode())


# Close the connection
client_socket.close()
server_socket.close()
