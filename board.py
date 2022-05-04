import pygame
from settings import *
from cell import Cell

class CreateBoard:
    def __init__(self, size):
        self.tile_size = size[0]
        self.rows = size[1][0]
        self.cols = size[1][1]
        self.matrix = [[0]*self.cols for row in range(self.rows)]
        self.surface = pygame.display.get_surface()
        self.board_surf = pygame.Surface((880, 500))
        self.board_surf.fill(DEAD_CELL)
        self.cells_list = []

        self.create_cells()
    
    def cell_status(self, row, col):
        neighbours = {'N':[0,-1],'S':[0,1],'E':[1,0],'W':[-1,0],'NE':[1,-1],'NW':[-1,-1],'SE':[1,1],'SW':[-1,1]}
        alive_neighbours = 0
        for direction in neighbours:
            x = neighbours[direction][0]
            y = neighbours[direction][1]
            if (0<= (row+x) < self.rows) and (0 <= (col+y) < self.cols):
                if self.matrix[row+x][col+y] == 1:
                    alive_neighbours += 1

        if (alive_neighbours < 2) or (3 < alive_neighbours):
            cell_new_status = 0
        elif (alive_neighbours==2):
            cell_new_status = self.matrix[row][col]
        else:
            cell_new_status = 1        
        return cell_new_status
    
    def next_step(self):
        next_matrix = [[0]*self.cols for row in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                next_matrix[row][col] = self.cell_status(row, col)
        self.matrix = next_matrix

    def create_cells(self):
        self.cells_list = []
        print('Creating cells..')
        for row_index,row in enumerate(self.matrix):
            for col_index,col in enumerate(row):
                x = col_index * self.tile_size[0]
                y = row_index * self.tile_size[0]
                cell = Cell((x, y), (self.tile_size), col)
                self.cells_list.append(cell)
        print(f'A total of {len(self.cells_list)} cells were created.')

    def update_cells(self):
        pass
    
    def run(self, click=None):
        if click:
            click = int(click[0]-((WIDTH/2)-440)),int(click[1]-120)
        # Draw the board
        self.surface.blit(self.board_surf,((WIDTH/2)-440,120))
        for cell in self.cells_list:
            cell.draw(self.board_surf)
            if click:
                if cell.rect.collidepoint(click):
                    cell_x = int(cell.pos[1]/self.tile_size[0])
                    cell_y = int(cell.pos[0]/self.tile_size[0])
                    if cell.status == 0:
                        cell.status = 1
                        self.matrix[cell_x][cell_y] = 1
                    else:
                        cell.status = 0
                        self.matrix[cell_x][cell_y] = 0