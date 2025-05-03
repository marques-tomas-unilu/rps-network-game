import socket

# Function to determine the winner between two moves
def determine_winner(move1, move2):
    if move1 == move2:
        return 0  # tie
    elif (move1 == "rock" and move2 == "scissors") or \
            (move1 == "scissors" and move2 == "paper") or \
            (move1 == "paper" and move2 == "rock"):
        return 1  # player 1 wins
    else:
        return 2  # player 2 wins

host = "localhost"
port = 6000

# Create and set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)  # Listen for two players
print("Server is running... Waiting for players.")

# Main server loop – runs forever to handle new games
while True:
    print("\nWaiting for two players to connect...")

    # Accept connection from Player 1
    conn1, addr1 = server_socket.accept()
    print("Player 1 connected from", addr1)
    conn1.send("You are Player 1\n".encode())

    # Accept connection from Player 2
    conn2, addr2 = server_socket.accept()
    print("Player 2 connected from", addr2)
    conn2.send("You are Player 2\n".encode())

    score1 = 0
    score2 = 0

    # Play 3 rounds of the game
    for round_number in range(1, 4):
        # Let Player 2 know they must wait
        conn2.send("Waiting for Player 1 to make a move...\n".encode())

        # Prompt Player 1 to enter their move
        conn1.send(f"\nRound {round_number}: Enter rock, paper or scissors: ".encode())
        move1 = conn1.recv(1024).decode().strip().lower()

        # Now prompt Player 2 after Player 1 has moved
        conn2.send(f"\nRound {round_number}: Player 1 has played. Now it's your turn: ".encode())
        move2 = conn2.recv(1024).decode().strip().lower()

        # Determine who won the round
        result = determine_winner(move1, move2)

        # Update scores and prepare round result message
        if result == 1:
            score1 += 1
            round_result = f"Player 1 wins this round! ({move1} vs {move2})"
        elif result == 2:
            score2 += 1
            round_result = f"Player 2 wins this round! ({move1} vs {move2})"
        else:
            round_result = f"It's a tie! ({move1} vs {move2})"

        # Send round result and score to both players
        message = f"{round_result}\nScore: Player 1 = {score1}, Player 2 = {score2}"
        conn1.send(message.encode())
        conn2.send(message.encode())

    # After 3 rounds, determine the game winner
    if score1 > score2:
        winner = "Player 1 wins the game!"
    elif score2 > score1:
        winner = "Player 2 wins the game!"
    else:
        winner = "The game is a tie!"

    # Send final result to both players
    final_message = f"\nFinal Score: Player 1 = {score1}, Player 2 = {score2}\n{winner}"
    conn1.send(final_message.encode())
    conn2.send(final_message.encode())

    # Close connections and restart the server for the next two players
    conn1.close()
    conn2.close()
    print("Game finished. Restarting server for new players...")
