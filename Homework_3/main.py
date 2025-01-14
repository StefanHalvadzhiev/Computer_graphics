import pygame
import sys
import math
from collections import deque

# Инициализация на Pygame
pygame.init()

# Параметри на прозореца
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
background_color = (0, 0, 0)
outer_circle_color = (0, 255, 0)  # Зелен за външния кръг
inner_circle_color = (0, 0, 255)  # Бял за вътрешния кръг
fill_color = (255, 0, 0)  # Червен за запълването

# Параметри за кръговете (различни центрове)
outer_center_x, outer_center_y = 400, 300
inner_center_x, inner_center_y = 600, 300
outer_radius = 200
inner_radius = 100

def draw_circles():
    pygame.draw.circle(screen, outer_circle_color, (outer_center_x, outer_center_y), outer_radius)
    pygame.draw.circle(screen, inner_circle_color, (inner_center_x, inner_center_y), inner_radius)

def is_within_area_outer(x, y):
    distance_to_outer = math.sqrt((x - outer_center_x) ** 2 + (y - outer_center_y) ** 2)
    distance_to_inner = math.sqrt((x - inner_center_x) ** 2 + (y - inner_center_y) ** 2)
    
    return distance_to_outer < outer_radius and distance_to_inner > inner_radius

def is_within_area_inner(x, y):
    distance_to_outer = math.sqrt((x - outer_center_x) ** 2 + (y - outer_center_y) ** 2)
    distance_to_inner = math.sqrt((x - inner_center_x) ** 2 + (y - inner_center_y) ** 2)
    
    return distance_to_outer > outer_radius and distance_to_inner < inner_radius


def fill_area(x, y, func):
    queue = deque([(x, y)])

    while queue:
        current_x, current_y = queue.popleft()

        if not func(current_x, current_y):
            continue

        if screen.get_at((current_x, current_y)) == fill_color:
            continue

        pygame.draw.rect(screen, fill_color, (current_x, current_y, 1, 1))
        pygame.display.update()

        queue.append((current_x + 1, current_y))  # Дясно
        queue.append((current_x - 1, current_y))  # Ляво
        queue.append((current_x, current_y + 1))  # Надолу
        queue.append((current_x, current_y - 1))  # Нагоре

# Основната функция
def main():
    running = True
    while running:
        screen.fill(background_color)
        
        # Рисуваме кръговете
        draw_circles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    mouse_x, mouse_y = event.pos

                    if is_within_area_outer(mouse_x, mouse_y):
                        fill_area(mouse_x, mouse_y, is_within_area_outer)

                    if is_within_area_inner(mouse_x, mouse_y):
                        fill_area(mouse_x, mouse_y, is_within_area_inner)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
