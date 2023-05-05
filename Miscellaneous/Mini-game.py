import pygame
import random

# Initialize pygame
pygame.init()

# Set the width and height of the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Catch Game")

# Set the clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 500
        self.speed = 5

    def update(self):
        # Get the current key state
        keys = pygame.key.get_pressed()

        # Move the player
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


# Object class
class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randint(2, 8)

    def update(self):
        # Move the object down the screen
        self.rect.y += self.speed

        # If the object goes off the bottom of the screen, reset it
        if self.rect.top > 600:
            self.rect.x = random.randrange(0, 750)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randint(2, 8)


# Create groups for all sprites and objects
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Create the objects
for i in range(10):
    obj = Object()
    all_sprites.add(obj)
    objects.add(obj)

# Set the score
score = 0

# Set the font
font_name = pygame.font.match_font("arial")


# Function to draw text on the screen
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# Game loop
running = True
while running:
    # Set the frame rate
    clock.tick(60)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for collisions between the player and objects
    hits = pygame.sprite.spritecollide(player, objects, True)
    for hit in hits:
        score += 1
        obj = Object()
        all_sprites.add(obj)
        objects.add(obj)

    # Draw everything on the screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, "Score: {}".format(score), 18, 50, 10)

    # Update the screen
    pygame.display.update()
