import pygame, sys
from settings import *
from board import CreateBoard
from board_options import BoardOptions
from debug import debug

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Conway's Game of Life")
        self.titleSurf = julius_sans_big.render("Conway's Game Of Life", 1, NEUTRAL)
        
        self.board = CreateBoard(SIZE['medium'])
        self.board_options = BoardOptions(self.board)
        self.game_active = 1

    def run(self):
        while True:
            click = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #print(f'Click at {pygame.mouse.get_pos()}')
                    click = pygame.mouse.get_pos()
            
            self.screen.fill(BACKGROUND)
            self.screen.blit(self.titleSurf,((WIDTH/2)-self.titleSurf.get_width()/2,50))
            if self.game_active:
                self.board.run(click)
                self.board_options.run(click)
            #debug('Testing debug display..')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
