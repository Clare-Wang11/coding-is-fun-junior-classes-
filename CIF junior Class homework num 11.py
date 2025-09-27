import pygame


# Initialize Pygame
pygame.init()
# Cap the frame rate
clock = pygame.time.Clock()
# Constants
SCREEN_WIDTH = 1800  # width
SCREEN_HEIGHT = 900  # height

PLAYER_X_POSITION = 0  # box_x
PLAYER_Y_POSITION = 840  # box_y

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60

PLAYER_X_CHANGE = 0
PLAYER_Y_CHANGE = 0
# FINISH_LINE_WIDTH = 20

# FINISH_LINE_HEIGHT = SCREEN_HEIGHT
BACKGROUND_COLOR_Black = (0, 0, 0)  # black
# PLAYER_COLOR = (0, 128, 255)
RED = (255, 0, 0)  # RED Lava
WALL_GRAY = (200, 200, 200)  # Wall
Water_blue = (0, 0, 255)
Boost_Green = (0, 255, 0)
Yellow_button = (100, 100, 0)
Portal_purple = (100, 0, 100)
# FINISH_LINE_COLOR = (0, 255, 0)
PLAYER_SPEED = 5

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Clare the Obstacle Course')

# Load player image
img = pygame.image.load("snowbunny.png")
img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))


myfont = pygame.font.SysFont('Algerian', 100)

# Set up complex maze obstacles
# Wall, Water, Portal, Lava, boost
obstacles = [
    ("wall", pygame.Rect(100, 100, 300, 20)),
    ("wall", pygame.Rect(400, 100, 20, 200)),
    ("portal", pygame.Rect(200, 200, 20, 200)),
    ("boost", pygame.Rect(300, 300, 300, 20)),
    ("portal", pygame.Rect(600, 300, 20, 200)),
    ("wall", pygame.Rect(400, 400, 200, 20)),
    ("water", pygame.Rect(100, 500, 400, 20)),
    ("lava", pygame.Rect(500, 100, 20, 200)),
    ("lava", pygame.Rect(100, 300, 100, 20)),
    ("lava", pygame.Rect(300, 600, 20, 200)),
    ("lava", pygame.Rect(400, 600, 300, 20)),
    ("lava", pygame.Rect(700, 100, 20, 700)),
    ("wall", pygame.Rect(800, 700, 300, 20)),
    ("boost", pygame.Rect(1000, 100, 20, 600)),
    ("portal", pygame.Rect(1200, 600, 300, 20)),
    ("wall", pygame.Rect(1500, 100, 20, 500)),
    ("wall", pygame.Rect(1700, 100, 20, 600)),
    ("wall", pygame.Rect(100, 800, 1600, 20)),
    ("button", pygame.Rect(0, 0, 30, 30))
]


def death():
    global PLAYER_X_POSITION, PLAYER_Y_POSITION, PLAYER_SPEED
    # Declare PLAYER X position and PLAYER Y position as global variables to modify them
    textsurface = myfont.render("Oops! You hit an obstacle.", False, (255, 255, 255))
    screen.fill(BACKGROUND_COLOR_Black)  # Fill the entire screen with the background color to clear previous drawing
    # Blit (draw) the rendered text onto the screen at the position (0, 0)
    screen.blit(textsurface, (0, 0))
    pygame.display.flip()   # Update the full display Surface to the screen
    print("ouch!!")
    PLAYER_X_POSITION = 0  # Set PLAYER X Position and PLAYER Y Position to 0, indicating the player is 'dead'
    PLAYER_Y_POSITION = 840
    PLAYER_SPEED = 7
    pygame.time.wait(1000)  # Pause the game for 1000 milliseconds (1 second) to give the player time to see the message


# Main game loop
while True:
    clock.tick(30)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()

    # Player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                PLAYER_X_CHANGE = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                PLAYER_X_CHANGE = PLAYER_SPEED
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                PLAYER_Y_CHANGE = -PLAYER_SPEED
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                PLAYER_Y_CHANGE = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                PLAYER_X_CHANGE = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                PLAYER_X_CHANGE = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                PLAYER_Y_CHANGE = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                PLAYER_Y_CHANGE = 0

    # Draw obstacles
    for ob in obstacles:
        if ob[0] == "wall":
            pygame.draw.rect(screen, WALL_GRAY, ob[1])
        elif ob[0] == "lava":
            pygame.draw.rect(screen, RED, ob[1])
        elif ob[0] == "water":
            pygame.draw.rect(screen, Water_blue, ob[1])
        elif ob[0] == "boost":
            pygame.draw.rect(screen, Boost_Green, ob[1])
        elif ob[0] == "portal":
            pygame.draw.rect(screen, Portal_purple, ob[1])
        elif ob[0] == "button":
            pygame.draw.rect(screen, Yellow_button, ob[1])

    PLAYER_X_POSITION += PLAYER_X_CHANGE
    if PLAYER_X_POSITION < 0:
        PLAYER_X_POSITION = 0
    if PLAYER_X_POSITION > SCREEN_WIDTH - PLAYER_WIDTH:
        PLAYER_X_POSITION = SCREEN_WIDTH - PLAYER_WIDTH
    for ob in obstacles:
        if img.get_rect(x=PLAYER_X_POSITION, y=PLAYER_Y_POSITION).colliderect(ob[1]):
            if ob[0] == "wall":
                PLAYER_X_POSITION -= PLAYER_X_CHANGE
            elif ob[0] == "lava":
                death()
            elif ob[0] == "water":
                PLAYER_SPEED = 1
            elif ob[0] == "boost":
                PLAYER_SPEED = 15
            elif ob[0] == "portal":
                PLAYER_X_POSITION = 0
            elif ob[0] == "button":
                PLAYER_X_POSITION = 0
                PLAYER_Y_POSITION = 840
                PLAYER_SPEED = 7

    PLAYER_Y_POSITION += PLAYER_Y_CHANGE
    if PLAYER_Y_POSITION < 0:
        PLAYER_Y_POSITION = 0
    if PLAYER_Y_POSITION > SCREEN_HEIGHT - PLAYER_HEIGHT:
        PLAYER_Y_POSITION = SCREEN_HEIGHT - PLAYER_HEIGHT
    for ob in obstacles:
        if img.get_rect(x=PLAYER_X_POSITION, y=PLAYER_Y_POSITION).colliderect(ob[1]):
            if ob[0] == "wall":
                PLAYER_Y_POSITION -= PLAYER_Y_CHANGE
            elif ob[0] == "lava":
                death()
            elif ob[0] == "water":
                PLAYER_SPEED = 1
                # PLAYER_Y_POSITION += PLAYER_Y_CHANGE
            elif ob[0] == "boost":
                PLAYER_SPEED = 15
            elif ob[0] == "portal":
                PLAYER_Y_POSITION = +40
            elif ob[0] == "button":
                PLAYER_X_POSITION = 0
                PLAYER_Y_POSITION = 840
                PLAYER_SPEED = 7

    # Update display

    screen.blit(img, (PLAYER_X_POSITION, PLAYER_Y_POSITION))
    pygame.display.flip()
    screen.fill(BACKGROUND_COLOR_Black)
