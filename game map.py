import pygame
import random as rm
from classes import Survivor
from perlin_noise import PerlinNoise
pygame.init()
# initializing variables and setting up the screen
WHITE = (255, 255, 255)
GREEN = (94, 157, 52)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (225, 190, 128)
caption = "Perlin Noise"
size = [1920, 1020]

screen = pygame.display.set_mode(size)
pygame.display.set_caption(caption)
Clock = pygame.time.Clock()
height = size[1]
width = size[0]
seed = rm.randint(0, 10000000000)
player_sprites = pygame.sprite.Group()

Player_Char = Survivor(5, 5)

player_sprites.add(Player_Char)

player_image = pygame.image.load("Survivor.png").convert_alpha()
player_scaled= pygame.transform.scale(player_image, (40, 60))

def proc_gen():
    # generating the map
    global map_list
    map_list = []
    noise = PerlinNoise(octaves = 1.5, seed = seed)
    block_size = 10  # Increase block size to reduce iterations
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            n = noise([x / width, y / height])
            g = int((n + 1) / 2 * 255)  # Scale noise value to 0-255
            if n < 0:
                g = GREEN
            elif n < 0.0042:
                g = YELLOW
            if g == GREEN:
                top_bottom = rm.randint(0, 4)
                mid = rm.randint(4,6)
                for i in range(top_bottom):
                    pygame.draw.rect(screen, GRAY, (x, y, block_size, block_size))
                for v in range(mid):
                    pygame.draw.rect(screen, GRAY, (x, y, block_size, block_size))
                pygame.draw.rect(screen, g, (x, y, block_size, block_size))
            pygame.draw.rect(screen, g , (x, y, block_size, block_size))
            num = round(n, 5)
            map_list.append(num)
            


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Over")
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player_Char.rect.x -= 10
    if keys[pygame.K_RIGHT]:
        Player_Char.rect.x += 10
    if keys[pygame.K_UP]:
        Player_Char.rect.y -= 10
    if keys[pygame.K_DOWN]:
        Player_Char.rect.y += 10
    
      # Clear the screen before drawing the new map
    screen.fill(WHITE)
    proc_gen()
    screen.blit(player_scaled,(Player_Char.rect.x, Player_Char.rect.y))
    pygame.display.update()
    player_sprites.update()
    pygame.display.flip()
    Clock.tick(1000)