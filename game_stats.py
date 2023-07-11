class GameStats():

    def __init__(self, ai_settings, ai_screen):
        self.settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
