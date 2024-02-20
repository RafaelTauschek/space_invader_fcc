import pygame

# Initalize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#Player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                
    player_x += player_x_change
    player(player_x, player_y)
    pygame.display.update()