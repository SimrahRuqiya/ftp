import socket

def connect_to_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))  # Connect to the server
    return sock

def send_file(sock):
    while True:
        filename = input("Enter the filename to transfer: ")
        try:
            with open(filename, 'rb') as file:
                data = file.read(1024)
                while data:
                    sock.send(data)
                    data = file.read(1024)
            break
        except IOError:
            print("Invalid file name or file not found. Please try again.")

def close_connection(sock):
    sock.close()  # Close the socket connection
    print("Connection closed.")

if __name__ == "__main__":
    host = "127.0.0.1" # localhost
    port = 8080 # port number for the server

    sock = connect_to_server(host, port)
    print("Connected to the server. You can now send files.")
    send_file(sock)  # Send a file to the server
    close_connection(sock)  # Close the connection