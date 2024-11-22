import pygame 
import pygame_menu
from src.player import Player
from src.cars import Cars

class Controller:
  def __init__(self):
    self.player = Player()
    self.cars = Cars()
    self

    #setup pygame data
    
  def mainloop(self):
    running = True
    while running: 
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False 

      player.update()

      if pygame.sprite.spritecollide(player, cars, False):
        print("Game Over!")
          
      self.screen.fill('black') 
      pygame.display.flip()



    pygame.sprite.spritecollide(self.player, self.cars)
    
    self.sprite
   
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    start = True
    while start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      gameDisplay.fill(white)
      largeText = pygame.font.Font('freesanbold.ttf', 115)
      TextSurf, TextRect = text_objects("Chicken Crossing", largeText)
      TextRect.center = ((display_width/2), (display_height/2))
      gameDisplay.bilt(TextSurf, TextRect)
      pygame.display.update()
      clock.tick(15)
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    self.background_image = pygame.image.load(background.png).convert()
    
  def mad():
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw