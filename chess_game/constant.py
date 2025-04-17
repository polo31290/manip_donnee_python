import pygame
import os

width, height = 760,760
rows, cols = 8, 8
square = width//rows


brown = (87,16,16)
white = (255,255,255)
green = (0, 153, 51)
grey = (192, 192, 192)

path = "img"

#black pieces
black_knight = pygame.transform.scale(pygame.image.load(os.path.join(path, "bKN.png")), (square, square))
black_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path, "bB.png")), (square, square))
black_king = pygame.transform.scale(pygame.image.load(os.path.join(path, "bK.png")), (square, square))
black_queen = pygame.transform.scale(pygame.image.load(os.path.join(path, "bQ.png")), (square, square))
black_tower = pygame.transform.scale(pygame.image.load(os.path.join(path, "bT.png")), (square, square))
black_pion = pygame.transform.scale(pygame.image.load(os.path.join(path, "bP.png")), (square, square))


#white pieces
white_knight = pygame.transform.scale(pygame.image.load(os.path.join(path, "wKN.png")), (square, square))
white_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path, "wB.png")), (square, square))
white_king = pygame.transform.scale(pygame.image.load(os.path.join(path, "wK.png")), (square, square))
white_queen = pygame.transform.scale(pygame.image.load(os.path.join(path, "wQ.png")), (square, square))
white_tower = pygame.transform.scale(pygame.image.load(os.path.join(path, "wT.png")), (square, square))
white_pion = pygame.transform.scale(pygame.image.load(os.path.join(path, "wP.png")), (square, square))