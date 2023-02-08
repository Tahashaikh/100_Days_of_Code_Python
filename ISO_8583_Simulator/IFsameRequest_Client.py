import socket


def client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('192.168.1.143', 12345)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    try:
        # Send a request
        request = b'ISO 8583 request'
        client_socket.sendall(request)
        print('Sent data: {}'.format(request))

        # Receive the response
        response = client_socket.recv(1024)
        print('Received data: {}'.format(response))
    finally:
        # Clean up the connection
        client_socket.close()
        print('Connection closed.')


if __name__ == '__main__':
    client()
