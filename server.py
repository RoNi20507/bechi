import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345  # Port number

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection.
server_socket.listen(5)

while True:
    # Establish connection with client.
    client_socket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))

    # Receive data from client
    data = client_socket.recv(1024).decode()
    received_numbers = [int(x) for x in data.split(',')]

    # Check if the received data is a list of four numbers
    if len(received_numbers) == 4:
        print("Received numbers:", received_numbers)
        # Process received data (optional)
        # For example, you can perform operations on the received numbers

        # Send response (optional)
        response = "Data received successfully"
        client_socket.send(response.encode())
    else:
        print("Received data does not contain four numbers.")
        response = "Invalid data format"
        client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
