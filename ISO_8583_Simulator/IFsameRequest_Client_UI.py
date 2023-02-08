from flask import Flask, request
import socket

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the server's address and port
        server_address = ('172.26.176.1', 12345)
        client_socket.connect(server_address)
        print('Connected to {}:{}'.format(*server_address))

        try:
            # Send a request
            request_data = request.form['request_data']
            client_socket.sendall(request_data.encode())
            print('Sent data: {}'.format(request_data))

            # Receive the response
            response = client_socket.recv(1024)
            print('Received data: {}'.format(response))
        finally:
            # Clean up the connection
            client_socket.close()
            print('Connection closed.')

        return 'Sent: {}<br>Received: {}'.format(request_data, response.decode())
    return '''
        <form method="post">
            Request data: <input type="text" name="request_data">
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == '__main__':
    app.run()
