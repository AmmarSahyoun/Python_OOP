import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

game = Game('student_folder/flappy_bird/bird.png', 'student_folder/flappy_bird/pipe.png', 'student_folder/flappy_bird/background.png', 'student_folder/flappy_bird/ground.png')
game.resize_images()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() # shutdown game completely

  game.show_background(screen)
      
  pygame.display.update()
  clock.tick(120)
