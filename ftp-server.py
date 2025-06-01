import socket

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

def receive_files(connections): # Function to receive files from clients
    fileNo = 0
    index = 0

    for conn in connections:
        index += 1
        dataRecieved = conn[0].recv(1024) # Receive data from the client

        if not dataRecieved:
            print("No data received from client", index)
            continue
        filename = 'output' + str(fileNo) # Create a filename for each file
        fileNo += 1

        with open(filename, 'wb') as file:
            file.write(dataRecieved) # Write the first chunk
            while True:
                data = conn[0].recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"File {filename} received from client {index}")

    for conn in connections: # Close all connections
        conn[0].close()

if __name__ == "__main__":
    host = "127.0.0.1" # localhost
    port = 8080 # port number for the server

    totalClients = int(input("Enter the number of clients: "))
    connections = start_server(host, port, totalClients)
    receive_files(connections)
    print("All files received and connections closed.")