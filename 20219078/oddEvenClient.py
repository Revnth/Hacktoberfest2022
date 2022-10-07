import socket

# IP Address of my system
IP = "192.168.10.127"
PORT = 4567
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """ Connecting to the server. """
    client.connect(ADDR)
    """ Opening and reading the file data. """
    data = input('Enter a number to send: ')
    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    """ Closing the connection from the server. """
    client.close()

if __name__ == "__main__":
    main()
