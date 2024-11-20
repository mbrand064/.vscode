class Background:
    def __init__(self, image_file, location):
        self.image = pygame.image.load("background_image.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def render(self, screen):
        screen.blit(self.image, self.rect)

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))

bg = Background('background_image.jpg', [0, 0])
