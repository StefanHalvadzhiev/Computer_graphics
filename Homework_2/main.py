import pygame
import sys
import math

pygame.init()

window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))

background_color = (255, 255, 255)
circle_color = (0, 0, 255)

pixel_size = 10

def put_pixel(x, y):
    pygame.draw.rect(screen, circle_color, (x, y, pixel_size, pixel_size))

def draw_bresenham_circle(center_x, center_y, radius):
    while radius >= 0:
        x = 0
        y = radius
        e = 1 - radius
        while(x <= y):
            eight_symmetric(center_x, center_y, x, y)
            if e >= 0:
                e = e + 2 * x - 2 * y + 5
                y -= 1
            else:
                e = e + 2 * x + 3
            four_symmetric(center_x, center_y, x, y)
            x += 1
        radius -= 1

def four_symmetric(xc, yc, x, y):
    put_pixel(xc + x, yc + y)
    put_pixel(xc - x, yc -y)
    put_pixel(xc - x, yc + y)
    put_pixel(xc + x, yc - y)


def eight_symmetric(xc, yc, x, y):
    four_symmetric(xc, yc, x, y)
    four_symmetric(xc, yc, y, x)


def main():
    # Център и радиус на окръжността (примерни стойности)
    center_x, center_y, radius = 400, 300, 100

    running = True
    while running:
        screen.fill(background_color)

        draw_bresenham_circle(center_x, center_y, radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
