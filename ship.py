import pygame
from pygame.sprite import Sprite

class Ship():
    '''Класс управления кораблем'''

    def __init__(self, ai_settings, ai_screen):
        """Initialize the ship, and set its starting position."""
        # super().__init__()
        self.screen = ai_screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load("images\\ship.bmp")
        # self.image = pygame.image.load("images\\mario.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = ai_screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        # self.rect.center = self.screen_rect.center  # center
        self.rect.bottom = self.screen_rect.bottom
        # self.center = float(self.rect.centerx)
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        '''Рисует корабль в этой позиции'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
