import pygame
from settings import *

class Button():
    def __init__(self, text:str, pos:tuple):
        self.str = text
        self.pos = pos
        self.text = julius_sans_small.render(text, 1, BACKGROUND, NEUTRAL)
        self.width = self.text.get_width()
        self.surf = pygame.Surface((self.width+4, 26))
        self.surf.fill(ALIVE_CELL)
        self.rect = self.surf.get_rect(topleft=self.pos)
    def render(self, surface, click=None, func=None):
        surface.blit(self.surf, self.pos)
        self.surf.blit(self.text, (2,2))
        if click:
            if self.rect.collidepoint(click):
                print(f'Clicked on {self.str} button')
                self.text = julius_sans_small.render(self.str, 1, NEUTRAL, ALIVE_CELL)
                self.surf.blit(self.text, (2,2))
                self.text = julius_sans_small.render(self.str, 1, BACKGROUND, NEUTRAL)
                if func:
                    print(f'Initializing {self.str} function')
                    func()

class BoardOptions():
    def __init__(self, board):
        self.board = board
        self.surface = pygame.display.get_surface()
        # Run button
        self.run_button = Button('Run', (1000, 650))
        self.running = 0
        # Pause button
        self.pause_button = Button('Pause', (900, 650))
        # Next gen button
        self.next_button = Button('Next Gen',(700,650))
        # Reset button
        self.reset_button  = Button('Reset', (100, 650))

    def next_action(self):
        self.board.next_step()
        self.board.create_cells()

    def run_action(self):
        self.running = 1
    
    def pause_action(self):
        self.running = 0
    
    def reset_action(self):
        self.running = 0
        self.board.matrix = [[0]*self.board.cols for row in range(self.board.rows)]
        self.board.create_cells()


    def run(self, click=None):
        self.run_button.render(self.surface, click, self.run_action)
        self.pause_button.render(self.surface, click, self.pause_action)
        self.next_button.render(self.surface, click, self.next_action)
        self.reset_button.render(self.surface, click, self.reset_action)
        if self.running:
            pygame.time.delay(50)
            self.next_action()