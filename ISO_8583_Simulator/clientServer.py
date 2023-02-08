import socket
import threading


def server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('ISO 8583 server is listening on {}:{}'.format(*server_address))

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        connection, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Receive the ISO 8583 message
        data = connection.recv(1024)
        print('Received data: {}'.format(data))

        # Echo the ISO 8583 message back to the client
        if data:
            connection.sendall(data)

        # Clean up the connection
        connection.close()
        print('Connection closed.')


def client(message):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    # Send the ISO 8583 message to the server
    client_socket.sendall(message)

    # Receive the echoed ISO 8583 message from the server
    data = client_socket.recv(1024)
    print('Received echoed data: {}'.format(data))

    # Clean up the connection
    client_socket.close()
    print('Connection closed.')


if __name__ == '__main__':
    message = b'ISO 8583 message'
    server_thread = threading.Thread(target=server)
    server_thread.start()
    client(message)
    server_thread.join()
