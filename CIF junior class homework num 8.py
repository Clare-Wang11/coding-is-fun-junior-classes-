import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

x = 0

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # DO STUFF HERE (HERE IS WHERE YOU WRITE YOUR GAME)
    # Clear the screen
    screen.fill((0, 0, 0))
    rect1 = pygame.Rect(x, 100, 50, 50)
    # Move the rectangle
    rect1.move_ip(2, 0)
    # Draw the rectangle
    pygame.draw.rect(screen, (255, 255, 255), rect1)
    pygame.display.update()
    # Update x to move the rectangle to the right
    x += 2
