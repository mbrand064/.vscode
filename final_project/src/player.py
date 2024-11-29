#Rectangle: w, h, pos 
#surface: contains rect, has image

class Player(pygame.sprite.Sprite): 
    def __init__(self,name):
        super().__init__()
        
        self.x = 50
        self.y = height / 2
        self.size = 'small'
        self.width = 100
        self.height = 50
        self.speed = 4
        self.player = pygame.image.load(f"/assets/{player}.png") 
        self.player = pygame.transform.scale(self.player, self.width, self.height)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
    def draw(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    



        
