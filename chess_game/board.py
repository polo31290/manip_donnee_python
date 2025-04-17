import pygame
from .pieces import *
from .constant import *


class nextboard:
    def __init__(self, width, height, rows, cols, square, win):
        self.width = width
        self.height = height
        self.square = square
        self.width = win
        self.rows = rows
        self.cols = cols
        self.board = []
        self.create_board()

    
    def create_board(self):
        for row in range(self.rows):
            self.board.append([0 for i in range(self.cols)])

            for col in range(self.cols):
                if row == 1:
                    self.board[row][col] = Pion(self.square, black_pion, black, "pion", row, col)

                if row == 6 :
                    self.board[row][col] = Pion(self.square, white_pion, white, "pion", row, col)

                
                if row == 0:
                    if col == 0 or col == 7 :
                        self.board[row][col] = tower(self.square, black_tower, black, "tour", row, col)

                    if col == 1 or col == 6 :
                        self.board[row][col] = knight(self.square, black_knight, black, "chevalier", row, col)

                    if col == 2 or col == 5 :
                        self.board[row][col] = bishop(self.square, black_bishop, black, "fou", row, col)

                    if col == 3 :
                        self.board[row][col] = queen(self.square, black_queen, black, "reine", row, col)

                    if col == 4 :
                        self.board[row][col] = king(self.square, black_king, black, "roi", row, col)



                if row == 7 :
                    if col == 0 or col == 7 :
                        self.board[row][col] = tower(self.square, white_tower, white, "tour", row, col)

                    if col == 1 or col == 6 :
                        self.board[row][col] = knight(self.square, white_knight, white, "chevalier", row, col)

                    if col == 2 or col == 5 :
                        self.board[row][col] = bishop(self.square, white_bishop, white, "fou", row, col)

                    if col == 3 :
                        self.board[row][col] = queen(self.square, white_queen, white, "reine", row, col)

                    if col == 4 :
                        self.board[row][col] = king(self.square, white_king, white, "roi", row, col)

                    
    def get_piece(self, row, col):
        return self.board[row][col]

    def move (self, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        piece.piece_move(row, col)

        if piece.type == "pion":
            if piece.first_move:
                piece.first_move = False


    def draw_board(self):
        self.win.fill(green)

        for in range(self.rows):
            for col in range(row%2, cols, 2):
                pygame.draw.rect(self.win, white, (square*(row), square*(col), square, square))


    def draw_piece(self, piece, win):
        win.blit(piece.image, (piece.x, piece.y))


    def draw_pieces(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 0:
                    self.draw_piece(self.board[row][col], self.win)

                    