# Bingo: A Networked GUI Game

This is a two-player, client-server Bingo game built using Python's `tkinter` for the graphical user interface (GUI) and the built-in `socket` library for network communication. Players can either **Create a game** (acting as the server) or **Join a game** (acting as the client) by specifying the server's IP address.

The goal is to mark five numbers in a row, column, or diagonal on your 5x5 grid to achieve a "strike". The first player to achieve five strikes wins the game.

## How to Play 

1.  **Start and Connect:**
    * One player launches the application and clicks **'Create a game'** to act as the server.
    * The second player enters the server's IP address and clicks **'Join a game'**.
    * Both players click **'Start Game'** to initiate the connection and begin play.

2.  **Turn-Based Gameplay:**
    * The server randomly determines which player goes first.
    * The player whose turn it is clicks a number on their 5x5 Bingo grid.
    * The chosen number is immediately **sent over the network** to the opponent.
    * The number is marked off (disabled and turned black) on **both** players' grids.
    * The turn passes to the opponent.

3.  **Scoring and Win Condition:**
    * When a player completes a line (row, column, or diagonal) of marked numbers, they score a **strike**.
    * The corresponding letter tiles (B, I, N, G, O) at the bottom of the grid turn **green** as strikes are earned.
    * The game ends when a player achieves 5 strikes.
---

### **Screenshots**

**First Frame of UI**


> **Status:** Game runs.
##### Comment: Can be improved with multithreading (to prevent the UI from freezing while waiting for a network response).

**In Game:** *Example of marked numbers and earned strikes.*

Player 1:  
![image](https://user-images.githubusercontent.com/78027710/188316178-6eeac2d8-4114-4e05-8c36-2edfe355a1a1.png)      
  
Player 2:  
![image](https://user-images.githubusercontent.com/78027710/188316195-d9ab0232-fbdd-420c-99bd-498f8af35347.png)
