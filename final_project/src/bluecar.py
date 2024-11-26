class BlueCar(pygame.sprite.Sprite): 
    def __init__(self, x, y, width, height, image, speed, direction): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = 'medium'
        self.image = pygame.image.load(f"/assets/{car}.png") 
        self.speed = speed
        self.direction = direction

    def update(self):
        if self.direction == "left": 
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed 
    
    def draw(self):
        display = pygame.display.get_surface()
        self.image
