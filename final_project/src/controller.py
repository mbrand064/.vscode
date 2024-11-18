import pygame 
from src.player import Player
from src.cars import Cars
from src.movingscreen import MovingScreen
class Controller:
  def __init__(self):
    self.player = Player()
    self.cars = Cars()
    self.obstacles = Obstacles()

    #setup pygame data
    
  #def mainloop(self):
    #while True: 
      fer ecent in pygame.event.get()
      self.screen.fill('blue') 


    pygame.sprite.spritecollide(self.player, self.cars)
    
    self.sprite
   
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
