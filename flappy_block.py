import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game settings
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -9
FPS = 60

# Load bird image
BIRD_IMG = pygame.transform.scale(pygame.image.load('block.png'), (BIRD_WIDTH, BIRD_HEIGHT))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Block')

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self):
        screen.blit(BIRD_IMG, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self):
        # Draw upper pipe
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        # Draw lower pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))

    def get_upper_rect(self):
        return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)

    def get_lower_rect(self):
        return pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)

def draw_welcome_screen():
    screen.fill(BLACK)
    title_text = font.render('Flappy Block', True, WHITE)
    start_text = font.render('Press SPACE to Start', True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

def draw_game_over_screen(score):
    screen.fill(BLACK)
    game_over_text = font.render('Game Over', True, WHITE)
    score_text = font.render(f'Score: {score}', True, WHITE)
    restart_text = font.render('Press ENTER to Restart', True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    pygame.display.flip()

def main():
    while True:
        bird = Bird()
        pipes = [Pipe(SCREEN_WIDTH + 100)]
        score = 0

        welcome_screen = True
        while welcome_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome_screen = False

            draw_welcome_screen()
            clock.tick(FPS)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.jump()

            bird.update()
            for pipe in pipes:
                pipe.update()

                if pipe.x + PIPE_WIDTH < 0:
                    pipes.remove(pipe)
                    pipes.append(Pipe(SCREEN_WIDTH))

                if pipe.x < bird.x and not pipe.passed:
                    score += 1
                    pipe.passed = True

                if bird.get_rect().colliderect(pipe.get_upper_rect()) or bird.get_rect().colliderect(pipe.get_lower_rect()):
                    running = False

            if bird.y > SCREEN_HEIGHT or bird.y < 0:
                running = False

            screen.fill(BLACK)
            bird.draw()

            for pipe in pipes:
                pipe.draw()

            score_text = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)

        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False

            draw_game_over_screen(score)
            clock.tick(FPS)

if __name__ == '__main__':
    main()
