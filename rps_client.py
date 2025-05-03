import socket

# Ask the user for the server IP address
host = input("Enter server IP (default: localhost): ") or "localhost"
port = 6000

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using the provided host and port
client_socket.connect((host, port))

# Main loop to receive and send messages
while True:
    # Receive a message from the server
    message = client_socket.recv(1024).decode()
    print(message)

    # If the server asks for a move, get input from the player and send it
    if "Enter rock" in message:
        move = input("Your move (rock, paper, or scissors): ")
        if move not in ["rock", "paper", "scissors"]:
            print("Invalid move! Please Enter rock, paper, or scissors.")
            continue
        client_socket.send(move.strip().lower().encode())

    # If the final score is sent, break the loop and close the connection
    if "Final Score" in message:
        break

# Close the socket connection to the server
client_socket.close()