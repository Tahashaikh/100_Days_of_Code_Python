import socket


def server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('0.0.0.0', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('ISO 8583 server is listening on {}:{}'.format(*server_address))

    # Pre-defined request
    expected_request = b'ISO 8583 request'

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        connection, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Receive the incoming request
        data = connection.recv(1024)
        print('Received data: {}'.format(data))

        # Check if the incoming request is the same as the pre-defined request
        if data == expected_request:
            # Respond with the same request
            connection.sendall(b"Created By Taha")
        else:
            # Respond with an "Invalid request" message
            connection.sendall(b'Invalid request')

        # Clean up the connection
        connection.close()
        print('Connection closed.')


if __name__ == '__main__':
    server()
