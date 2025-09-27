import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1060
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
FINISH_LINE_WIDTH = 20
FINISH_LINE_HEIGHT = SCREEN_HEIGHT
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
OBSTACLE_COLOR = (0, 0, 255)
FINISH_LINE_COLOR = (0, 255, 0)
PLAYER_SPEED = 9

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Obstacle Course')

# Load player image
img = pygame.image.load("snowbunny.png")
img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Set up player
player = pygame.Rect(50, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Set up complex maze obstacles
obstacles = [
    pygame.Rect(100, 100, 300, 20),
    pygame.Rect(400, 100, 20, 200),
    pygame.Rect(200, 200, 200, 20),
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(300, 300, 300, 20),
    pygame.Rect(600, 300, 20, 200),
    pygame.Rect(400, 400, 200, 20),
    pygame.Rect(100, 500, 400, 20),
    pygame.Rect(500, 100, 20, 200),
    pygame.Rect(100, 300, 100, 20),
    pygame.Rect(300, 600, 20, 200),
    pygame.Rect(400, 600, 300, 20),
    pygame.Rect(700, 100, 20, 700),
    pygame.Rect(800, 700, 300, 20),
    pygame.Rect(1000, 100, 20, 600),
    pygame.Rect(1200, 600, 300, 20),
    pygame.Rect(1500, 100, 20, 500),
    pygame.Rect(1700, 100, 20, 600),
    pygame.Rect(100, 800, 1600, 20)
]

# Set up finish line
finish_line = pygame.Rect(SCREEN_WIDTH - FINISH_LINE_WIDTH, 0, FINISH_LINE_WIDTH, FINISH_LINE_HEIGHT)

# Set up font
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += PLAYER_SPEED

    # Boundary conditions
    if player.x < 0:
        player.x = 0
    if player.y < 0:
        player.y = 0
    if player.x > SCREEN_WIDTH - PLAYER_WIDTH:
        player.x = SCREEN_WIDTH - PLAYER_WIDTH
    if player.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
        player.y = SCREEN_HEIGHT - PLAYER_HEIGHT

    # Collision detection
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            textsurface = myfont.render("Oops! You hit an obstacle.", False, (255, 0, 0))
            screen.blit(textsurface, (0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            player.x, player.y = 50, SCREEN_HEIGHT - PLAYER_HEIGHT  # Reset player position
            break

    if player.colliderect(finish_line):
        textsurface = myfont.render("Congratulations! You've reached the finish line.", False, (0, 255, 0))
        screen.blit(textsurface, (0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw player
    screen.blit(img, (player.x, player.y))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    # Draw finish line
    pygame.draw.rect(screen, FINISH_LINE_COLOR, finish_line)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
