#Rectangle: w, h, pos 
#surface: contains rect, has image

class Player(pygame.sprite.Sprite): 
    def __init__(self,name):
        super().__init__()
        
        self.name
        self.size = 'small'
        self.image = pygame.image.load(f"/assets/{name}.png") 
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    #ur gonna want to stop and go and such and screen moves 
    #def jump(self):
       #

   #def update(self:
   # self.rect.x -=2 