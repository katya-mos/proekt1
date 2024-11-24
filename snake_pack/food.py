import pygame
import random

class Food:
    """Класс для еды в игре."""
    
    def __init__(self):
        """Инициализация еды."""
        self.position = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)
        self.color = (255, 0, 0)  # Начальный цвет - красный
        self.points = 3  # Начальные очки
    
    def spawn(self):
        """Генерация новой еды с случайным цветом и очками."""
        colors = {
            (255, 0, 0): 3,
            (255, 255, 0): 2,
            (0, 255, 0): 1,
        }
        
        self.color = random.choice(list(colors.keys()))
        self.points = colors[self.color]
        
        self.position = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)

    def draw(self, surface):
        """Отрисовка еды на экране."""
        pygame.draw.rect(surface, self.color, (*self.position, 20, 20))
