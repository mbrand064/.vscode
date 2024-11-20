import pygame 
from src.player import Player
from src.cars import Cars
from src.movingscreen import MovingScreen
class Controller:
  def __init__(self):
    self.player = Player()
    self.cars = Cars()
    self.music = Music()
    self

    #setup pygame data
    
  #def mainloop(self):
    #while True: 
      for event in pygame.event.get()
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
