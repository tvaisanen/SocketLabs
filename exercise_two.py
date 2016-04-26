from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import argparse, sys

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", help="Port to use", type=int)
    args = parser.parse_args()
    return args

host = ''
data_payload = 2048
backlog = 5


def echo_server(port):

    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_address = (host, port)
    print('Starting the server @ {}:{}'.format(host, port))
    sock.bind(server_address)
    sock.listen(backlog)
    while True:
        try:
            print('Waiting for messages..')
            client, address = sock.accept()
            message = client.recv(data_payload)
            if message:
                print('Message: {}'.format(message))
                client.send(message)
                print('Echoed: {} to {}.'.format(message, address))
            client.close()
        except KeyboardInterrupt:
            sys.exit(1)

if __name__ == '__main__':
    args = handle_arguments()
    port = args.port
    echo_server(port)
