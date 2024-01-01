import pygame
import sys
import random
import os

# Initialisez Pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('image/1.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (1, 0)  
        self.color = BLUE

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        current = self.get_head_position()
        x, y = self.direction
        new = ((current[0] + (x * SNAKE_SIZE)) % WIDTH, (current[1] + (y * SNAKE_SIZE)) % HEIGHT)

        # Si le serpent touche la pomme
        if new == apple.position:
            self.length += 1
            apple.randomize_position()

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def reset(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (1, 0)


class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.rect = pygame.Rect(0, 0, SNAKE_SIZE, SNAKE_SIZE)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
            random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
        )

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))


class AI:
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple

    def update(self):
        
        head_position = self.snake.get_head_position()
        apple_position = self.apple.position

        if head_position[0] < apple_position[0]:
            self.snake.set_direction((1, 0))  # Déplacer vers la droite
        elif head_position[0] > apple_position[0]:
            self.snake.set_direction((-1, 0))  # Déplacer vers la gauche
        elif head_position[1] < apple_position[1]:
            self.snake.set_direction((0, 1))  # Déplacer vers le bas
        elif head_position[1] > apple_position[1]:
            self.snake.set_direction((0, -1))  # Déplacer vers le haut

def render_text(surface, text, position, color):
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")  

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    global apple
    apple = Apple()
    ai = AI(snake, apple)

    best_score = 0  

    
    score_file_path = "best_score.txt"

    
    if os.path.exists(score_file_path):
        with open(score_file_path, 'r') as file:
            best_score = int(file.read())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        ai.update()

        snake.update()

        
        if snake.get_head_position() in snake.positions[1:]:
            print("Game Over! Your Score:", snake.length - 1)
            if snake.length - 1 > best_score:
                best_score = snake.length - 1
                print("New Best Score:", best_score)

                
                with open(score_file_path, 'w') as file:
                    file.write(str(best_score))

            
            snake.reset()
            apple.randomize_position()

        
        screen.blit(background, (0, 0))

        snake.render(screen)
        apple.render(screen)

        
        render_text(screen, f"Score: {snake.length - 1}", (20, 20), RED)
        render_text(screen, f"Best Score: {best_score}", (20, 70), RED)

        
        clock.tick(snake.length + 5)

        pygame.display.update()

    
    with open(score_file_path, 'w') as file:
        file.write(str(best_score))

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()