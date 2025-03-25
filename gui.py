import pygame
from board import Board

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Jeu d'Échecs")
        self.board = Board()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.board.handle_click(x // 50, y // 50)

            self.screen.fill((255, 255, 255))
            self.board.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
