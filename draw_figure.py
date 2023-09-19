import pygame
def draw_cross(screen, x, y,size_block, cross_widht, white, mas, row, col):
    if mas[row][col] == "x":
        pygame.draw.line(screen, white, (x + 50, y + 50), (x + size_block - 50, y + size_block - 50), cross_widht)
        pygame.draw.line(screen, white, (x + size_block - 50, y + 50), (x + 50, y + size_block - 50), cross_widht)

def draw_circle(screen, x, y,size_block, circle_radius,circle_width, white, mas, row, col):
    if mas[row][col] == "o":
        pygame.draw.circle(screen, white, (x + size_block//2, y + size_block//2), circle_radius, circle_width)
