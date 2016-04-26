from socket import socket, AF_INET, SOCK_STREAM
import argparse, sys

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("IP", help="IP address to send the message", type=str)
    parser.add_argument("port", help="Port to use", type=int)
    parser.add_argument("message", help="Message to send")
    args = parser.parse_args()
    return args

def createConnection(address_):
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.bind(address_)
    except Exception as e:
        print(str(e))
    return sock

def sendMessageAndClose(socket_, message_):
    encoded_message = message_.encode('utf-8')
    try:
        socket_.send(encoded_message)
    except Exception as e:
        print(str(e))
    socket_.close()

def main():
    first_try = True
    try:
        if first_try:
            args = handle_arguments()
            address = (args.IP, args.port)
            first_try = False
        else:
            IP = input("IP-osoite: ")
            port = input("Portti: ")
            address = (IP, port)
        message = args.message
        sock = createConnection(address)

    except KeyboardInterrupt as e:
        print("Ohjelma lopetetaan.")
        sys.exit(1)

if __name__ == '__main__':
    main()



