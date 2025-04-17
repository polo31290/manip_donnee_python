import pygame
from .constant import *

class Piece:
    def __init__(self, square, image, color, type, row, col):
        self.square = square
        self.image = image
        self.color = color
        self.row = row
        self.col = col
        self.type = type
        self.x = 0
        self.y = 0
        self.availables_moves = []

    def piece_move (self, row,col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*self.square
        self.y = self.row*self.square

    def clear_availables_moves(self):
        if len(self.availables_moves) >0:
            self.availables_moves = []


            
class Pion(piece):
    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)
        self.first_move = True

    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()

        if self.color == white:
            if row-1 >= 0:
                if board[row-1][col] == 0:
                    self.availables_moves.append((row-1, col))
                if self.first_moves :
                    if board[row-1][col] == 0 and board[row-2][col] == 0:
                        self.availables_moves.append((row-2, col))
                if col-1 >=0 :
                    if board[row-1][col-1] != 0:
                        piece = board[row-1][col-1]
                        if piece.color != self.color:
                            self.availables_moves.append((row-1, col-1))

                if col+1 < len(board[0]):
                    if board[row-1][col+1] != 0:
                        piece = board[row-1][col-1]

                        if piece.color != self.color:
                            self.availables_moves.append((row-1, col+1))


        if self.color == black:
            if row+1 < len(board):
                if board[row+1][col] ==0:
                    self.availables_moves.append((row+1, col))

                if self.first_move:
                    if board[row+1][col] ==0 and board[row+2][col] == 0:
                        self.availables_moves.append((row+2, col))

                if col-1 >= 0 :
                    if board[row+1][col-1] != 0:
                        piece = board[row+2][col-1]
                        if piece.color != self.color :
                            self.availables_moves.append((row+1, col-1))


                if col+1 < len(board):
                    if board[row+1][col+1] != 0 :
                        piece = board[row+1][col+1]

                        if piece.color != self.color :
                            self.availables_moves.append((row+1, col+1))


    return self.availables_moves()

class tower(piece):
    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)
    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()
        for i in range(row+1, 8):
            if board[i][col] == 0:
                self.availables_moves.append((i, col))
            else :
                if board[i][col].color != self.color:
                    self.availables_moves.append((i, col))
                    break
                else: 
                    break
        for j in range(row-1, -1,-1):
            if board[j][col] ==0:
                self.availables_moves.append((j, col))
            else:
                if board[j][col].color != self.color:
                    self.availables_moves.append((j,col))
                    break
                else:
                    break
        for i in range(col+1, 8):
            if board[row][i] ==0 :
                self.availables_moves.append((row, i))
            else:
                if board[row][i].color != self.color :
                    self.availables_moves.append((row, i))
                    break
                else:
                    break
        for i in range(col-1,-1,-1):
            if board[row][i] ==0 :
                self.availables_moves.append((row, i))
            else:
                if board[row][i].color != self.color :
                    self.availables_moves.append((row, i))
                    break
                else:
                    break
    return self.availables_moves()


class bishop(piece):

    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)

    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()

        row_i = row+1
        col_i = col+1

        while row_i <= 7 and col_i <= 7 :
            if board[row_i][col_i] ==0 :
                self.availables_moves.append((row_i, col_i))
                row_i += 1
                col_i += 1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row-1
        col_i = col-1

        while row_i >= 0 and col_i >= 0 :
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i -=1
                col_i -=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row+1
        col_i = col-1
        while row_i <= 7 and col_i >= 0 :
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i +=1
                col_i -=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row-1
        col_i = col+1
        while row_i >= 0 and col_i <= 7:
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i -=1
                col_i +=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        return self.availables_moves()



class knight(piece):

    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)

    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()

        if row-2 >= 0 and col+1 < len(board):
            if board[row-2][col+1] == 0 or board[row-2][col+1].color != self.color :
                self.availables_moves.append((row-2, col+1))

        if row-1 >= 0 and col+2 < len(board[0]):
            if board[row-1][col+2] == 0 or board[row-1][col+2].color != self.color:
                self.availables_moves.append((row-1, col+2))

        if row+1 < len(board) and col+2 < len(board):
            if board[row+1][col+2] == 0 or board[row+1][col+2].color != self.color:
                self.availables_moves.append((row+1, col+2))

        if row+2 < len(board) and col+1 < len(board):
            if board[row+2][col+1] == 0 or board[row+2][col+1].color != self.color:
                self.availables_moves.append((row+2, col+1))


        if row+2 < len(board) and col-1 >= 0 :
            if board[row+2][col-1] == 0 or board[row+2][col-1].color != self.color:
            self.availables_moves.append((row+2, col-1))

        if row+1 < len(board) and col-2 >= 0 :
            if board[row+1][col-2] == 0 or board[row+1][col-2].color != self.color:
            self.availables_moves.append((row+1, col-2))

        if row-1 >= 0 and col -2 >=0:
            if board[row-1][col-2] == 0 or board[row-1][col-2].color != self.color:
                self.availables_moves.append((row-1, col-2))

        if row-2 >=0 and col -1 >=0:
            if board[row-2][col-1] == 0 or board[row-2][col-1].color != self.color:
                self.availables_moves.append((row-2, col-1))

    return self.availables_moves()



class queen(piece):

    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)

    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()


        while row_i <= 7 and col_i <= 7 :
            if board[row_i][col_i] ==0 :
                self.availables_moves.append((row_i, col_i))
                row_i += 1
                col_i += 1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row-1
        col_i = col-1

        while row_i >= 0 and col_i >= 0 :
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i -=1
                col_i -=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row+1
        col_i = col-1
        while row_i <= 7 and col_i >= 0 :
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i +=1
                col_i -=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break

        row_i = row-1
        col_i = col+1
        while row_i >= 0 and col_i <= 7:
            if board[row_i][col_i] == 0:
                self.availables_moves((row_i, col_i))
                row_i -=1
                col_i +=1

            else :
                if board[row_i][col_i].color != self.color :
                    self.availables_moves.append((row_i, col_i))

                    break

                else: 
                    break


        for i in range(row+1, 8):
            if board[i][col] == 0:
                self.availables_moves.append((i, col))
            else :
                if board[i][col].color != self.color:
                    self.availables_moves.append((i, col))
                    break
                else: 
                    break
        for j in range(row-1, -1,-1):
            if board[j][col] ==0:
                self.availables_moves.append((j, col))
            else:
                if board[j][col].color != self.color:
                    self.availables_moves.append((j,col))
                    break
                else:
                    break
        for i in range(col+1, 8):
            if board[row][i] ==0 :
                self.availables_moves.append((row, i))
            else:
                if board[row][i].color != self.color :
                    self.availables_moves.append((row, i))
                    break
                else:
                    break
        for i in range(col-1,-1,-1):
            if board[row][i] ==0 :
                self.availables_moves.append((row, i))
            else:
                if board[row][i].color != self.color :
                    self.availables_moves.append((row, i))
                    break
                else:
                    break
    return self.availables_moves()



class king(piece):

    def __init__(self, square, image, color, type, row, col):
        super().__init__(square, image, color, type, row, col)

    def get_available_moves(self, row, col, board):
        self.clear_availables_moves()

        if row-1 >=0:
            if board[row-1][col] == 0 or board[row-1][col].color != self.color:
                self.availables_moves.append((row-1, col))

        if row -1 >=0 and col +1 < len(board) :
            if board[row-1][col+1] == 0 or board[row-1][col+1].color != self.color:
                self.availables_moves.append((row-1, col+1))


        if col +1 < len(board):
            if board[row][col+1] == 0 or board[row][col+1].color != self.color:
                self.availables_moves.append((row, col+1))

        if row+1 < len(board) and col+1 < len(board):
            if board[row+1][col+1] == 0 or board[row+1][col+1].color != self.color:
                self.availables_moves.append((row+1, col+1))

        if row+1 < len(board):
            if board[row+1][col] == 0 or board[row+1][col].color != self.color:
                self.availables_moves.append((row+1, col))

        if row+1 < len(board) and col-1 >= 0:
            if board[row+1][col-1] == 0 or board[row+1][col-1].color != self.color:
                self.availables_moves.append((row+1, col-1))

        if col-1 >= 0 :
            if board[row][col-1] == 0 or board[row][col-1].color != self.color:
                self.availables_moves.append((row, col-1))

        if row-1 >= 0 and col-1 >=0 :
            if board[row-1][col-1] == 0 or board[row-1][col-1].color != self.color:
                self.availables_moves.append((row-1, col-1))