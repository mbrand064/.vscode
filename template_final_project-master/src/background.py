class Background:
    def __init__(self, image_file, location):
        self.image = pygame.image.load("background_image.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def render(self, screen):
        screen.blit(self.image, self.rect)

    



bg = Background('background.jpg', [0, 0])
