import pygame
import random

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
MINES = 10
CELL_SIZE = WIDTH // COLS
FONT_SIZE = 24

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont(None, FONT_SIZE)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

    def draw(self, screen):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
        if self.is_revealed:
            if self.is_mine:
                pygame.draw.circle(screen, BLACK, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 3)
            else:
                text = font.render(str(self.adjacent_mines), True, BLACK)
                screen.blit(text, (x + CELL_SIZE // 3, y + CELL_SIZE // 3))
        elif self.is_flagged:
            pygame.draw.rect(screen, RED, rect)

def create_grid(rows, cols, mines):
    grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
    mine_positions = set()
    while len(mine_positions) < mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if (row, col) not in mine_positions:
            mine_positions.add((row, col))
            grid[row][col].is_mine = True
    for row in range(rows):
        for col in range(cols):
            if not grid[row][col].is_mine:
                grid[row][col].adjacent_mines = sum(
                    grid[r][c].is_mine
                    for r in range(row - 1, row + 2)
                    for c in range(col - 1, col + 2)
                    if 0 <= r < rows and 0 <= c < cols
                )
    return grid

def reveal_cell(grid, row, col):
    if grid[row][col].is_revealed or grid[row][col].is_flagged:
        return
    grid[row][col].is_revealed = True
    if grid[row][col].adjacent_mines == 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < ROWS and 0 <= c < COLS and not grid[r][c].is_mine:
                    reveal_cell(grid, r, c)

def main():
    grid = create_grid(ROWS, COLS, MINES)
    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if event.button == 1:
                    if grid[row][col].is_mine:
                        game_over = True
                        for row in range(ROWS):
                            for col in range(COLS):
                                grid[row][col].is_revealed = True
                    else:
                        reveal_cell(grid, row, col)
                elif event.button == 3:
                    grid[row][col].is_flagged = not grid[row][col].is_flagged
        screen.fill(GRAY)
        for row in range(ROWS):
            for col in range(COLS):
                grid[row][col].draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
