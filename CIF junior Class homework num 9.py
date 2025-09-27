import pygame
import random

pygame.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
width = 800
height = 600
box_x = 50
box_y = 200
box_height = 50
box_width = 50
screen = pygame.display.set_mode((width, height))
box_x_change = 0
box_y_change = 0
speed = 5

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color = random_color()
frame_counter = 0

running = True
while running:
    clock.tick(30)
    frame_counter += 1
    if frame_counter == 30:
        color = random_color()
        frame_counter = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_x_change = -speed
            if event.key == pygame.K_RIGHT:
                box_x_change = speed
            if event.key == pygame.K_UP:
                box_y_change = -speed
            if event.key == pygame.K_DOWN:
                box_y_change = speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                box_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                box_y_change = 0

    box_x += box_x_change
    box_y += box_y_change
    if box_x < 0:
        box_x = 0
    if box_y < 0:
        box_y = 0
    if box_x > width - box_width:
        box_x = width - box_width
    if box_y > height - box_height:
        box_y = height - box_height

    screen.fill(black)
    rect1 = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, color, rect1)
    pygame.display.update()

pygame.quit()