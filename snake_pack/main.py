"""Главный файл для запуска игры "Змейка"."""

from snake_pack.game import Game

def main():
    """Главная функция для запуска игры."""
    game_instance = Game()
    game_instance.run()

if __name__ == "__main__":
    main()
