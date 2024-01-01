import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")



current_image_index = 0

background = pygame.image.load('image/0.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


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

        
        if new == apple.position:
            self.length += 1
            apple.randomize_position()

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))


class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.rect = pygame.Rect(0, 0, SNAKE_SIZE, SNAKE_SIZE)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

def main():
    clock = pygame.time.Clock()
    surface = pygame.Surface(screen.get_size()).convert()

    snake = Snake()
    global apple
    apple = Apple()

    best_score = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        snake.update()

        
        if (
            snake.get_head_position() in snake.positions[1:]
            or snake.get_head_position()[0] < 0
            or snake.get_head_position()[0] >= WIDTH
            or snake.get_head_position()[1] < 0
            or snake.get_head_position()[1] >= HEIGHT
        ):
            print("Game Over! Your Score:", snake.length - 1)
            if snake.length - 1 > best_score:
                best_score = snake.length - 1
                print("New Best Score:", best_score)
            pygame.quit()
            sys.exit()

    
        

        screen.blit(background, (0, 0))


        snake.render(screen)
        apple.render(screen)


        
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {snake.length - 1}", True, RED)
        best_score_text = font.render(f"Best Score: {best_score}", True, RED)

        screen.blit(score_text, (20, 20))
        screen.blit(best_score_text, (20, 70))


        
        clock.tick(snake.length + 5)

        pygame.display.update()

if __name__ == "__main__":
    main()
