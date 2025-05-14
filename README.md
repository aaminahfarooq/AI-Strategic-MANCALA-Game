# 🎮 AI-Strategic-MANCALA-Game

This is a Mancala game with an AI opponent, implemented using Python and Tkinter for the graphical user interface (GUI). The AI uses the Minimax algorithm with Alpha-Beta Pruning to make optimal moves. The game allows two players to play Mancala, where Player 1 is a human and Player 2 is controlled by the AI.
---

## 📊 Dataset

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size**: 284,807 transactions
- **Features**: 30 features (V1–V28 PCA components, Time, Amount) + 1 Target (`Class`)
- **Target**: 
  - `0` → Legitimate
  - `1` → Fraudulent

---



🎮 How to Play

Player 1 (Human): Select a pit from pits 0-5 to make a move.

AI Player: The AI will automatically make a move based on the best possible decision using the Minimax algorithm.

The game continues until no moves are possible, and the winner is determined based on the stones in the stores, or if one of the players has 0 stones.

Game Interface:
The game board is displayed with 12 pits (6 for each player) and 2 stores (one for each player).

Each pit shows the number of stones in it.

Players can click a pit to make a move.

The game announces the winner when it ends.



⚙️ How It Works (AI Logic)

The AI player (Player 2) uses the Minimax algorithm with Alpha-Beta Pruning to choose the best move. Here's a breakdown of how it works:

-Minimax Algorithm: The algorithm recursively explores all possible moves for both players, evaluates the resulting board states, and chooses the move that maximizes the AI's score while minimizing the human player's score.

-Alpha-Beta Pruning: This optimization technique helps cut off branches in the game tree that don't need to be explored, improving the efficiency of the Minimax algorithm.

-Heuristic: The heuristic evaluation used for scoring the game state is the difference in the number of stones between the AI's store and the human player's store.



📌 Acknowledgements

Python and Tkinter for the programming and GUI.

Minimax Algorithm and Alpha-Beta Pruning for AI decision-making.
