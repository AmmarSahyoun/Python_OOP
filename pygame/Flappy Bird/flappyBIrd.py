import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

game = Game('bird.png', 'pipe.png', 'background.png', 'ground.png')
game.resize_images()

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1800)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() # shutdown game completely
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and game.active:
        game.flap()
    if event.type == SPAWNPIPE:
      game.add_pipe()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and game.active:
        game.flap()
            
      if event.key == pygame.K_SPACE and game.active == False:
        game.restart()
        
  game.show_background(screen)
      


      
  pygame.display.update()
  clock.tick(120)
