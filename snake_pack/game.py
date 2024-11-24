import pygame
import random
from .snake import Snake
from .food import Food

class Game:
    """Класс для управления игрой."""
    
    def __init__(self):
        """Инициализация игры."""
        pygame.init()
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def run(self):
        """Запуск игрового цикла."""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.snake.handle_event(event)

            self.snake.move()
            if self.snake.eat(self.food):
                self.score += self.food.points
                self.food.spawn()

            if self.snake.check_collision():
                running = False
            
            self.draw()
        
        pygame.quit()
    
    def draw(self):
        """Отрисовка элементов на экране."""
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Отображение счета
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Счет: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
