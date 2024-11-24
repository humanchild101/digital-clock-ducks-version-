import pygame

class SpriteSheet():
    def __init__(self, image):
        self.img = image

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.img, (0, 0), (width * frame, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image