from typing import Tuple
import pygame
from settings import *

class Cell():
    def __init__(self, pos:Tuple, size:Tuple, status) -> None:
        self.pos = pos
        self.size = size
        self.status = status
        self.face = pygame.Surface(size)
        self.rect = self.face.get_rect(topleft=self.pos)

    def draw(self, surf):
        if self.status == 0:
            self.face.fill(BACKGROUND)
            pygame.draw.rect(self.face, DEAD_CELL, ((1,1),(self.size[0]-2,self.size[0]-2)))
        else:
            self.face.fill(BACKGROUND)
        surf.blit(self.face, self.pos)