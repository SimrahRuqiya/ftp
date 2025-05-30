import socket

if __name__ == "__main__":
    host = "127.0.0.1" # localhost
    port = 8080 # port number for the server

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port)) # Connect to the server

    while True:
        filename = input("Enter the filename to transfer: ")

        try:
            file = open(filename, 'r') # Open the file to read
            data = file.read()

            if not data:
                break
            while data:
                sock.send(str(data).encode()) # Send data to the server
                data = file.read()
            file.close()
        except IOError:
            print("Invalid file name or file not found. Please try again.")

