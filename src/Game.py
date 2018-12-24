import pygame

from src.Config import Config
from src.Snake import Snake


class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        clock = pygame.time.Clock()
        snake = Snake(self.display)

        x_change = 0
        y_change = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -Config['snake']['speed']
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = Config['snake']['speed']

            # Fill background and draw game area
            self.display.fill(Config['colors']['green'])

            pygame.draw.rect(
                self.display,
                Config['colors']['black'],
                [
                    Config['game']['bumper_size'],
                    Config['game']['bumper_size'],
                    Config['game']['height'] - Config['game']['bumper_size'] * 2,
                    Config['game']['width'] - Config['game']['bumper_size'] * 2
                ]
            )

            # Draw an apple

            # Initialize font and draw title and score text
            pygame.font.init()
            font = pygame.font.Font('./assets/Now-Regular.otf', 28)

            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, Config['colors']['white'])
            title = font.render('Anaconda', True, Config['colors']['white'])

            title_rect = title.get_rect(
                center=(
                    Config['game']['width'] / 2,
                    Config['game']['bumper_size'] / 2
                )
            )

            score_rect = score.get_rect(
                center=(
                    500/2,
                    Config['game']['height'] - Config['game']['bumper_size'] / 2
                )
            )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)


            snake.move(x_change, y_change)
            snake.draw()

            pygame.display.update()
            clock.tick(Config['game']['fps'])
