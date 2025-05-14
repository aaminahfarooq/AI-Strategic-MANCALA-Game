import tkinter as tk
from tkinter import messagebox

# Mancala board representation
class Mancala_Board:
    def __init__(self, board=None):
        if board:
            self.mancala = board[:]
        else:
            # 6 pits per player + 1 store per player
            self.mancala = [4] * 6 + [0] + [4] * 6 + [0]  # Index 6 = P1 store, 13 = P2 store

    def player_move(self, pit_index):
        stones = self.mancala[pit_index]
        if stones == 0:
            return False  # Invalid move
        self.mancala[pit_index] = 0
        index = pit_index
        while stones > 0:
            index = (index + 1) % 14
            # Skip opponent's store
            if (pit_index < 6 and index == 13) or (pit_index > 6 and index == 6):
                continue
            self.mancala[index] += 1
            stones -= 1

        # Extra turn
        if (pit_index < 6 and index == 6) or (pit_index > 6 and index == 13):
            return True

        # Capture rule
        if self.mancala[index] == 1:
            if pit_index < 6 and 0 <= index < 6:
                opposite = 12 - index
                self.mancala[6] += self.mancala[opposite] + 1
                self.mancala[opposite] = 0
                self.mancala[index] = 0
            elif pit_index > 6 and 7 <= index < 13:
                opposite = 12 - index
                self.mancala[13] += self.mancala[opposite] + 1
                self.mancala[opposite] = 0
                self.mancala[index] = 0

        return False

    def available_moves(self, player):
        if player == 1:
            return [i for i in range(6) if self.mancala[i] > 0]
        else:
            return [i for i in range(7, 13) if self.mancala[i] > 0]

    def isEnd(self):
        return all(x == 0 for x in self.mancala[0:6]) or all(x == 0 for x in self.mancala[7:13])

    def collect_remaining_stones(self):
        if all(x == 0 for x in self.mancala[0:6]):
            for i in range(7, 13):
                self.mancala[13] += self.mancala[i]
                self.mancala[i] = 0
        elif all(x == 0 for x in self.mancala[7:13]):
            for i in range(0, 6):
                self.mancala[6] += self.mancala[i]
                self.mancala[i] = 0

    def husVal(self):
        return self.mancala[13] - self.mancala[6]

# GUI update
def update_display(board, labels):
    for i in range(14):
        labels[i].config(text=str(board.mancala[i]))

# GUI Class
class Mancala_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mancala Game")
        self.board = Mancala_Board()
        self.labels = []
        for i in range(14):
            label = tk.Label(self.root, text=str(self.board.mancala[i]), width=4, height=2, relief="solid", font=('Arial', 14))
            label.grid(row=0, column=i)
            self.labels.append(label)

        self.buttons = []
        for i in range(6):
            button = tk.Button(self.root, text=f"Pit {i+1}", command=lambda i=i: self.player_turn(i))
            button.grid(row=1, column=i)
            self.buttons.append(button)

        update_display(self.board, self.labels)

    def player_turn(self, i):
        if self.board.mancala[i] == 0:
            messagebox.showwarning("Invalid Move", "Choose a pit with stones!")
            return

        repeat_turn = self.board.player_move(i)
        update_display(self.board, self.labels)

        if self.board.isEnd():
            self.board.collect_remaining_stones()
            update_display(self.board, self.labels)
            winner = self.get_winner()
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.root.quit()

        if not repeat_turn and not self.board.isEnd():
            self.ai_turn()

    def ai_turn(self):
        best_move = self.minimax(self.board, 3, True, -float('inf'), float('inf'))
        self.board.player_move(best_move)
        update_display(self.board, self.labels)

        if self.board.isEnd():
            self.board.collect_remaining_stones()
            update_display(self.board, self.labels)
            winner = self.get_winner()
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.root.quit()
        else:
            self.show_turn_prompt()

    def get_winner(self):
        p1 = self.board.mancala[6]
        p2 = self.board.mancala[13]
        return "Player 1" if p1 > p2 else "Player 2" if p2 > p1 else "Draw"

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        if depth == 0 or board.isEnd():
            return board.husVal()

        if maximizing_player:
            max_eval = -float('inf')
            best_move = None
            for move in board.available_moves(2):
                board_copy = Mancala_Board(board.mancala)
                board_copy.player_move(move)
                eval = self.minimax(board_copy, depth - 1, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return best_move if depth == 3 else max_eval
        else:
            min_eval = float('inf')
            for move in board.available_moves(1):
                board_copy = Mancala_Board(board.mancala)
                board_copy.player_move(move)
                eval = self.minimax(board_copy, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def show_turn_prompt(self):
        messagebox.showinfo("Your Turn", "Your turn to play!")

# Start Game
if __name__ == "__main__":
    root = tk.Tk()
    game = Mancala_GUI(root)
    root.mainloop()
