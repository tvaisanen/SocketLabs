from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import argparse, sys

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("SMTP", help="SMTP-server address", type=String)
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = handle_arguments()

    SMTP_IP = args.SMTP
    SMTP_PORT = 25
    SMTP_ADDRESS = (SMTP_IP, SMTP_PORT)
    BUFF = 2046

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(SMTP_ADDRESS)
    hello_from_server = sock.recv(BUFF)
    print(hello_from_server)
    sock.send('HELO \r\n'.encode('utf-8'))
    received = sock.recv(BUFF)
    if receive:
        # do something





"""
Open TCP socket
Connect socket to SMTP server address, port 25
Read server hello from socket
Send HELO command
Read response, check that return code is valid or exit
Read sender address from stdin
Send MAIL command
Read response, check that return code is valid or exit
Read recipient address from stdin
Send RCPT command
Read response, check that return code is valid or exit
Read message subject from stdin
Read message content from stdin
Send DATA command
Read response, check that return code is valid or exit
Send message
Read response, check that return code is valid or exit
Send QUIT command
Read response, check that return code is valid or exit
Close the TCP socket
"""