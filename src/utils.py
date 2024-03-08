import pygame
from enum import Enum
from config import SCREEN, BODY


class Utils:
    def render_font(
        self,
        content: str,
        font: pygame.font.Font = BODY,
        antialias: bool = True,
        color: pygame.Color = pygame.Color(255, 255, 255),
        background: pygame.Color = pygame.Color(0, 0, 0, 0),
        **kwargs
    ):
        """Function to render font into a specified destination using kwargs. Will render at 0, 0 if no dest value is specified."""
        text = font.render(content, antialias, color, background)
        text_rect = text.get_rect(**kwargs)
        SCREEN.blit(text, text_rect)

    class GameStatus(Enum):
        MENU = "MENU"
        PLAYING = "PLAYING"
