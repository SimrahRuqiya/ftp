import socket
import os

def connect_to_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))  # Connect to the server
    return sock

def send_files(sock):
    files_to_send = []

    while True:
        filename = input("Enter a filename to transfer (or 'done' to finish): ")
        if filename.lower() == 'done':
            break
        if os.path.isfile(filename):
            files_to_send.append(filename)
        else:
            print("File not found. Try again.")

    sock.send(len(files_to_send).to_bytes(4, 'big'))  

    for filename in files_to_send:
        basename = os.path.basename(filename)
        filesize = os.path.getsize(filename)

        # Send filename length, filename, and filesize
        sock.send(len(basename).to_bytes(4, 'big'))
        sock.send(basename.encode())
        sock.send(filesize.to_bytes(8, 'big'))  # 8 bytes for large files

        # Send file content
        with open(filename, 'rb') as f:
            while (data := f.read(1024)):
                sock.send(data)

        print(f"{basename} ({filesize} bytes) sent successfully.")

def close_connection(sock):
    sock.close()  # Close the socket connection
    print("Connection closed.")

if __name__ == "__main__":
    host = "127.0.0.1" # localhost
    port = 8080 # port number for the server

    sock = connect_to_server(host, port)
    print("Connected to the server! You can now send files.")
    send_files(sock)  # Send a file to the server
    close_connection(sock)  # Close the connection