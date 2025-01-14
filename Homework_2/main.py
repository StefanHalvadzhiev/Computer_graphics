import pygame
import sys

pygame.init()

window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))

background_color = (255, 255, 255)
input_color_inactive = (200, 200, 200)
input_color_active = (0, 255, 0)
text_color = (0, 0, 0)

pixel_size = 5

font = pygame.font.Font(None, 36)

# Функция за рисуване на пиксел
def put_pixel(x, y, color):
    pygame.draw.rect(screen, color, (x, y, pixel_size, pixel_size))

# Функция за рисуване на окръжност с алгоритъма на Брезенхем
def draw_bresenham_circle(center_x, center_y, radius, color):
    x = 0
    y = radius
    e = 1 - radius
    while x <= y:
        eight_symmetric(center_x, center_y, x, y, color)
        if e >= 0:
            e = e + 2 * x - 2 * y + 5
            y -= 1
        else:
            e = e + 2 * x + 3
        four_symmetric(center_x, center_y, x, y, color)
        x += 1

# Функция за рисуване на четирите симетрични точки
def four_symmetric(xc, yc, x, y, color):
    put_pixel(xc + x, yc + y, color)
    put_pixel(xc - x, yc - y, color)
    put_pixel(xc - x, yc + y, color)
    put_pixel(xc + x, yc - y, color)

# Функция за рисуване на осемте симетрични точки
def eight_symmetric(xc, yc, x, y, color):
    four_symmetric(xc, yc, x, y, color)
    four_symmetric(xc, yc, y, x, color)

# Функция за обработка на въвеждане на текст
def get_input_box(font, x, y, width, height, prompt, color):
    input_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, input_box)
    input_text = font.render(prompt, True, text_color)
    screen.blit(input_text, (x + 5, y + 5))
    return input_box

def main():
    center_x, center_y, radius = 400, 300, 100
    color = (0, 0, 255)
    input_color = f"{color[0]},{color[1]},{color[2]}"

    active_center_x, active_center_y, active_radius, active_color = False, False, False, False
    text_center_x, text_center_y, text_radius, text_color = '', '', '', input_color

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                active_center_x = pygame.Rect(50, 50, 200, 50).collidepoint(event.pos)
                active_center_y = pygame.Rect(50, 110, 200, 50).collidepoint(event.pos)
                active_radius = pygame.Rect(50, 170, 200, 50).collidepoint(event.pos)
                active_color = pygame.Rect(50, 230, 200, 50).collidepoint(event.pos)

            if event.type == pygame.KEYDOWN:

                if active_center_x:
                    if event.key == pygame.K_RETURN:
                        try:
                            center_x = int(text_center_x)
                        except ValueError:
                            text_center_x = 'Invalid'
                        text_center_x = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_center_x = text_center_x[:-1]
                    else:
                        text_center_x += event.unicode
                elif active_center_y:
                    if event.key == pygame.K_RETURN:
                        try:
                            center_y = int(text_center_y)
                        except ValueError:
                            text_center_y = 'Invalid'
                        text_center_y = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_center_y = text_center_y[:-1]
                    else:
                        text_center_y += event.unicode
                elif active_radius:
                    if event.key == pygame.K_RETURN:
                        try:
                            radius = int(text_radius)
                        except ValueError:
                            text_radius = 'Invalid'
                        text_radius = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_radius = text_radius[:-1]
                    else:
                        text_radius += event.unicode
                elif active_color:
                    if event.key == pygame.K_RETURN:
                        try:
                            color = tuple(map(int, text_color.split(',')))
                        except ValueError:
                            text_color = 'Invalid'
                        text_color = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_color = text_color[:-1]
                    else:
                        text_color += event.unicode

        screen.fill(background_color)

        draw_bresenham_circle(center_x, center_y, radius, color)

        get_input_box(font, 50, 50, 200, 50, f'Center X: {text_center_x}', input_color_active if active_center_x else input_color_inactive)
        get_input_box(font, 50, 110, 200, 50, f'Center Y: {text_center_y}', input_color_active if active_center_y else input_color_inactive)
        get_input_box(font, 50, 170, 200, 50, f'Radius: {text_radius}', input_color_active if active_radius else input_color_inactive)
        get_input_box(font, 50, 230, 200, 50, f'Color (R,G,B): {text_color}', input_color_active if active_color else input_color_inactive)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
