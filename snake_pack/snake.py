import pygame

class Snake:
    """Класс для змейки в игре."""
    
    def __init__(self):
        """Инициализация змейки."""
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (20, 0)

    def handle_event(self, event):
        """Обработка событий клавиатуры для управления змейкой."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != (0, 20):
                self.direction = (0, -20)
            elif event.key == pygame.K_DOWN and self.direction != (0, -20):
                self.direction = (0, 20)
            elif event.key == pygame.K_LEFT and self.direction != (20, 0):
                self.direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and self.direction != (-20, 0):
                self.direction = (20, 0)

    def move(self):
        """Движение змейки."""
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        
    def eat(self, food):
        """Проверка поедания еды."""
        if self.body[0] == food.position:
            self.body.append(self.body[-1])  # Увеличение размера
            return True
        return False

    def check_collision(self):
        """Проверка столкновения со стенами или самим собой."""
        head_x, head_y = self.body[0]
        
        if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
            return True
        
        if len(self.body) > 1 and (head_x, head_y) in self.body[1:]:
            return True
        
        return False

    def draw(self, surface):
        """Отрисовка змейки на экране."""
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (*segment, 20, 20))
