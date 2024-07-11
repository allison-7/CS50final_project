# Flappy Block Game in Python using Pygame

This is based off of the Flappy Bird game using the Pygame library in Python.

## Video Demo
https://youtu.be/2VQajY5JqEo

## Table of Contents
- [Game Description](#game-description)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Pygame Initialization and Setup](#pygame-initialization-and-setup)
  - [Screen and Color Definitions](#screen-and-color-definitions)
  - [Game Settings](#game-settings)
  - [Load Bird Image](#load-bird-image)
  - [Create the Screen](#create-the-screen)
  - [Clock and Font](#clock-and-font)
  - [Bird Class](#bird-class)
  - [Pipe Class](#pipe-class)
  - [Draw Welcome Screen](#draw-welcome-screen)
  - [Draw Game Over Screen](#draw-game-over-screen)
  - [Main Function](#main-function)
- [Running the Game](#running-the-game)

## Game Description
Flappy Block is a side-scrolling game where the player controls a block, attempting to fly between columns of green pipes without hitting them. The game continues until the block collides with a pipe or the ground.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/allison-7/CS50final_project.git
    cd CS50final_project
    ```
2. Install Pygame:
    ```sh
    pip install pygame
    ```

## Usage
Run the game:
```sh
python flappy_block.py
```

## Code Explanation

### Pygame Initialization and Setup
```python
import pygame
import random

# Initialize Pygame
pygame.init()
```
- **Pygame Initialization**: Pygame is initialized to set up the library for use.

### Screen and Color Definitions
```python
# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
```
- **Screen Dimensions**: The width and height of the game window are defined.
- **Colors**: RGB values for common colors used in the game are defined.

### Game Settings
```python
# Game settings
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -9
FPS = 60
```
- **Game Settings**: Constants are defined for the bird's size, pipe's size, gap between pipes, gravity, and jump strength.

### Load Bird Image
```python
# Load bird image
BIRD_IMG = pygame.transform.scale(pygame.image.load('bird.png'), (BIRD_WIDTH, BIRD_HEIGHT))
```
- **Load Bird Image**: The bird image is loaded and scaled to the defined width and height.

### Create the Screen
```python
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Block')
```
- **Create the Screen**: A window with the specified dimensions is created, and its title is set to "Flappy Block".

### Clock and Font
```python
# Clock object to control the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)
```
- **Clock Object**: Used to control the frame rate of the game.
- **Font**: Defines the font and size used for displaying text in the game.

### Bird Class
```python
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
```
- **Bird Class**: Represents the bird in the game.
    - **__init__**: Initializes the bird's position and velocity.
    - **update**: Updates the bird's position based on gravity.
    - **jump**: Sets the bird's velocity for jumping.
    - **draw**: Draws the bird on the screen.
    - **get_rect**: Returns the bird's rectangle for collision detection.

### Pipe Class
```python
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
```
- **Pipe Class**: Represents the pipes in the game.
    - **__init__**: Initializes the pipe's position and random height.
    - **update**: Moves the pipe to the left.
    - **draw**: Draws the upper and lower pipes on the screen.
    - **get_upper_rect** and **get_lower_rect**: Return the rectangles of the upper and lower pipes for collision detection.

### Draw Welcome Screen
```python
def draw_welcome_screen():
    screen.fill(BLACK)
    title_text = font.render('Flappy Bird', True, WHITE)
    start_text = font.render('Press SPACE to Start', True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
```
- **draw_welcome_screen**: Displays the welcome screen with the title and start message.

### Draw Game Over Screen
```python
def draw_game_over_screen(score):
    screen.fill(BLACK)
    game_over_text = font.render('Game Over', True, WHITE)
    score_text = font.render(f'Score: {score}', True, WHITE)
    restart_text = font.render('Press ENTER to Restart', True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    pygame.display.flip()
```
- **draw_game_over_screen**: Displays the game over screen with the final score and restart message.

### Main Function
```python
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
            clock.tick(30)

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
            clock.tick(30)

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
            clock.tick(30)

if __name__ == '__main__':
    main()
```



### Main Function Detailed Breakdown

1. **Infinite Loop**:
   - The game runs inside an infinite loop to allow restarting after a game over.

2. **Initialize Bird and Pipes**:
   - A bird object and a list of pipes are created.
   - The score is initialized to 0.

3. **Welcome Screen Loop**:
   - Displays the welcome screen and waits for the player to press the space bar to start the game.

4. **Game Loop**:
   - Handles events (like quitting and jumping).
   - Updates the bird's position and the pipes.
   - Checks for collisions and updates the score.
   - Ends the game if the bird collides with a pipe or goes out of bounds.
   - Draws the bird, pipes, and score on the screen.

5. **Game Over Loop**:
   - Displays the game over screen and waits for the player to press the space bar to restart the game.

6. **Run Main Function**:
   - The main function is executed if the script is run directly.

## Running the Game
To run the game, execute the following command:
```sh
python flappy_block.py
```

Enjoy playing Flappy Block!