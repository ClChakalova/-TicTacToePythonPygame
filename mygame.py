import pygame
import sys
from draw_figure import draw_circle
from draw_figure import draw_cross
from check_win import check_win


pygame.init()
size_block = 160
margin = 15
width = heigth = size_block*3 + margin*4
circle_radius = 40
circle_width = 15
cross_widht = 20

BG_color = (23, 145, 135)

red = (145, 23, 74)
blue = (23, 49, 145)
white = (255, 255, 255)

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("КРЕСТИКИ-НОЛИКИ (Чакалова Клавдия)")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
screen.fill(BG_color)

mas = [[0]*3 for i in range(3)]
query = 0 # 1 2 3 4 5 6 7
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query%2==0:
                  mas[row][col] = "x"
                else:
                  mas[row][col] = "o"
                query+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query=0
            screen.fill(BG_color)

    if not game_over:
        for row in range(3):
            for col in range(3):
              if mas[row][col]== "x":
                  color = red
              elif mas[row][col]== "o":
                  color = blue
              else:
                  color = white
              x = col*size_block + (col+1)*margin
              y = row * size_block + (row + 1) * margin
              pygame.draw.rect(screen, color, (x,y,size_block,size_block))
              if color==red:
                  draw_cross(screen, x, y, size_block, cross_widht, white, mas, row, col)
              elif color == blue:
                  draw_circle(screen, x, y, size_block, circle_radius, circle_width, white, mas, row, col)
    if (query-1)%2==0:#x
       game_over = check_win(mas, "x")

    else:
        game_over = check_win(mas, "o")


    if game_over:
        screen.fill(BG_color)
        font = pygame.font.SysFont('stxingkai', 30)
        text1 = font.render(f'Победитель - {game_over} ! Начать снова - <r> ', True, (white))
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()