import numpy as np
from src.config import *

class Connect4:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.current_player = 1
        self.game_over = False
        self.running = True
    
    def restart(self):
        self = Connect4()
    
    def no_moves(self):
        return np.all(self.board != 0)

    def drop_piece(self, col):
        for row in range(ROWS - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                if self.check_win(row, col):
                    return True
                self.current_player = 3 - self.current_player
                return True
        return False
    
    def check_win(self, row, col):
        player = self.board[row][col]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in [1, -1]:
                r, c = row + dr * d, col + dc * d
                while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == player:
                    count += 1
                    r += dr * d
                    c += dc * d
                if count >= 4:
                    return True
        return False
