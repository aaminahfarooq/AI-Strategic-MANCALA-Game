# 🎮 AI-Strategic-Mancala-Game
---
This is a Mancala game with an AI opponent, implemented using Python and Tkinter for the graphical user interface (GUI). The AI uses the Minimax algorithm with Alpha-Beta Pruning to make optimal moves. The game allows two players to play Mancala, where Player 1 is a human and Player 2 is controlled by the AI.
---

## 🕹️ Game Description
Mancala/African Chess is an ancient two-player strategy board game. The goal of the game is to capture more stones in your store than your opponent. The board consists of two rows, each containing 6 pits and a store for each player.

- **Pits**: There are 12 pits (6 for each player).
- **Stores**:  Each player has one store, located at the ends of the board.
- **Players**: Players take turns to pick a pit and distribute its stones across the board in a counter-clockwise direction.

---
## 🎮 Game Workflow and interface

1. **Workflow**
   -Player 1 (Human): Select a pit from pits 0-5 to make a move.
   
   -AI Player: The AI will automatically make a move based on the best possible decision using the Minimax algorithm.
   
   -The game continues until no moves are possible, and the winner is determined based on the stones in the stores, or if one of the players has 0 stones.

   
 2.**Game Interface**
   -The game board is displayed with 12 pits (6 for each player) and 2 stores (one for each player).
   
   -Each pit shows the number of stones in it.
   
   -Players can click a pit to make a move.
   
   -The game announces the winner when it ends.

---

## 🚀 Features
- **Interactive GUI**: Built using Tkinter for easy interaction.
- **AI Opponent**: AI uses the Minimax algorithm with Alpha-Beta pruning for decision-making.
- **Valid Move Check**: Players can only make valid moves (select pits with stones).
- **End Game Detection**: The game automatically ends when no more valid moves are available, the pits of one of the players is 0, and the winner is declared based on the number of stones in the stores.
- **Store Collection**: When one player’s pits are empty, the other player collects all the stones from their pits into their store.

---


## ⚙️ How It Works (AI Logic)
The AI player (Player 2) uses the Minimax algorithm with Alpha-Beta Pruning to choose the best move. Here's a breakdown of how it works:
- **Minimax Algorithm**: The algorithm recursively explores all possible moves for both players, evaluates the resulting board states, and chooses the move that maximizes the AI's score while minimizing the human player's score.
- **Alpha-Beta Pruning**: This optimization technique helps cut off branches in the game tree that don't need to be explored, improving the efficiency of the Minimax algorithm.
- **Heuristic**: The heuristic evaluation used for scoring the game state is the difference in the number of stones between the AI's store and the human player's store.

---

## 🛠️ Libraries Used
- tkinter
- from tkinter import messagebox

---
## 📌Acknowledgements
   -Python and Tkinter for the programming and GUI.
   
   -Minimax Algorithm and Alpha-Beta Pruning for AI decision-making.

---
## 📄 License
This project is for educational purposes only. Refer to the dataset license on Kaggle.

---
## ✍️ Author
Aaminah Binte Farooq – 2025








