import socket
import os 

def start_server(host, port, totalClients): # Pass arguments explicitly
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #AF_INET = address family is IPv4, socket type is TCP
    #SOCK_STREAM = connection-oriented tcp protocol

    sock.bind((host, port)) # Bind the socket to the host and port
    sock.listen(totalClients) # Listen for incoming connections

    connections = []
    print("Server started, waiting for connections..")

    for i in range(totalClients): # Loop to accept multiple clients
        conn = sock.accept() # Accept a connection
        connections.append(conn) 

        print("Connection established with client", i + 1)
    return connections # Return the list of connections

def unique_filename(directory, filename):
    base, ext = os.path.splitext(filename) # Split the filename into base and extension
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(directory, new_filename)): # Check if the file already exists
        new_filename = f"{base}({counter}){ext}" 
        counter += 1

    return new_filename

def receive_files(connections):
    save_dir = "received"
    os.makedirs(save_dir, exist_ok=True)

    for index, conn in enumerate(connections, start=1): 
        num_files_bytes = conn[0].recv(4) # Receive the number of files to expect
        if not num_files_bytes:
            print(f"No data received from client {index}") 
            continue
        num_files = int.from_bytes(num_files_bytes, 'big')  # Convert bytes to integer
        print(f"Receiving {num_files} file(s) from client {index}...") 

        for i in range(num_files):
            # Receive filename
            filename_len = int.from_bytes(conn[0].recv(4), 'big')
            filename = conn[0].recv(filename_len).decode()

            # Receive filesize
            filesize = int.from_bytes(conn[0].recv(8), 'big')

            # Receive the file data
            unique_filename_path = unique_filename(save_dir, filename)
            full_path = os.path.join(save_dir, unique_filename_path)
            with open(full_path, 'wb') as f:
                bytes_received = 0
                while bytes_received < filesize:
                    data = conn[0].recv(min(1024, filesize - bytes_received))
                    if not data:
                        break
                    f.write(data)
                    bytes_received += len(data)

            print(f"File {unique_filename_path} received ({filesize} bytes) from client {index}")

        conn[0].close()

    print("All files received and connections closed.")


if __name__ == "__main__":
    host = "127.0.0.1" # localhost
    port = 8080 # port number for the server

    totalClients = int(input("Enter the number of clients: "))
    connections = start_server(host, port, totalClients)
    receive_files(connections)