import socket

# IP Address of my system
IP = "192.168.10.127"
print(IP)
PORT = 4567
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)
    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")
    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)

        print(f"[RECV] Receiving the data from server")
	# Logic
        if int(data)%2 == 0:
                print(f"[CLIENT]: {data}")
                conn.send("Even Number".encode(FORMAT))
        else:
                conn.send("Odd Number".encode(FORMAT))
        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
