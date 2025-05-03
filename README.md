# Rock-Paper-Scissors (Multiplayer over Network)

This is a simple multiplayer Rock-Paper-Scissors game that you can play with another person over a local network. It uses Python's socket programming to connect a server and two clients.

## How the Game Works

- One person runs the **server**.
- Two players connect to the server using the **client**.
- The game has 3 rounds.
- Each round:
  - Player 1 sends their move first.
  - Player 2 sends their move after Player 1.
  - The server compares the moves and tells both players who won the round.
- After 3 rounds, the server announces the final score and the winner.

Moves can be:
- `rock`
- `paper`
- `scissors`

The rules are:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same move is a tie

## How to Run

### Requirements
- Python 3.x
- No extra libraries are needed

### Step 1: Start the Server
Run the following in a terminal:

```bash
python rps_server.py 
```

### Step 2: Start the Clients
Run the following in a terminal:

```bash
python rps_client.py
```

You will be asked to enter the IP address of the server. If the server is on the same computer, just press Enter to use the default (localhost).

## Notes
- The game supports only two players at a time.
- The server automatically restarts for the next two players after a game finishes.
