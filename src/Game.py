import pygame

from src.Config import Config
from src.Snake import Snake
from src.Apple import Apple


class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        clock = pygame.time.Clock()
        snake = Snake(self.display)
        apple = Apple(self.display)

        x_change = 0
        y_change = 0

        self.score = 0

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
            apple_rect = apple.draw()

            # Move and re-draw Snake
            snake.move(x_change, y_change)
            snake_rect = snake.draw()
            snake.draw_body()

            # Detect collison with wall
            bumper_x = Config['game']['width'] - Config['game']['bumper_size']
            bumper_y = Config['game']['height'] - Config['game']['bumper_size']

            if(
                snake.x_pos < Config['game']['bumper_size'] or
                snake.y_pos < Config['game']['bumper_size'] or
                snake.x_pos + Config['snake']['width'] > bumper_x or
                snake.y_pos + Config['snake']['height'] > bumper_y
            ):
                self.loop()

            # Detect collision with apple
            if apple_rect.colliderect(snake_rect):
                apple.randomize()
                self.score += 1
                snake.eat()

            # Collide with self
            if len(snake.body) >= 1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        self.loop()

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

            pygame.display.update()
            clock.tick(Config['game']['fps'])
