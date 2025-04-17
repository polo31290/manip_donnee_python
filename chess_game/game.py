import pygame
from .board import nextboard
from .constant import *
from copy import deepcopy


class Game :
    def __init__(self, width, height, rows, cols, square, win):
        self.win = win
        self.board = nextboard(width, height, rows, cols, square, win)
        self.square = square
        self.selected = None
        self.turn = white
        self.valide_moves = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16


    def update_window(self):
        self.board.draw_board()
        self.board.draw_pieces()
        self.draw_available_moves()
        pygame.display.update()


    def reset(self):
        self.board = nextboard(width, height, rows, cols, square, win)
        self.selected = None
        self.black_pieces_left, self.white_pieces_left = 16, 16
        self.valide_moves = []


    def change_turne(self):
        if self.turn == white:
            self.turn = black
        else:
            self.turn = white

    def select(self, row, col):
        if self.selected:
            move = self._move(row, col)

            if not move :
                self.selected = None
                self.selected(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and self.turn == piece.color:
            self.selected = piece


            self.valide_moves = piece.get_available_moves(row, col, self.board.board)


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected and (row, col) in self.valide_moves:
            if piece == 0 or piece.color != self.selected.color:
                if self.simulate_move(self.selected, row, col):
                    self.remoe(self.selected, row, col)

                    self.board.move(self.board.board, piece, row, col)
                    self.change_turn()
                    self.valide_moves = []
                    self.selected = None
                    return True 
                return False


    def remove(self, board, piece, row, col):
        if piece != 0 :
            board[row][col] = 0
            if piece.color == white:
                self.white_pieces_left -= 1
            else : 
                self.black_pieces_left -= 1 


    def draw_available_moves(self):
        if len(select.valide_moves) > 0 :
            for pos in self.valide_moves :
                row, col = pos[0], pos[1]
                pygame.draw.circle(self.win, grey, (col*self.square + self.square//2, row*self.square//2), self.square//8)
        
