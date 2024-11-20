class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y)
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.y = y 

coin_group = pygame.sprite.Group()

for coin in coin_group: 
    if pygame
