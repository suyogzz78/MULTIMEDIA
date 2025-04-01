import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 400
TABLE_COLOR = (39, 119, 20)  # Greenish table color
BALL_COLOR = (255, 255, 255)  # White ball
HOLE_COLOR = (0, 0, 0)  # Black holes (not yet used)
BALL_RADIUS = 10
BALL_MASS = 1
FRICTION = 0.01  # Slows down movement over time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pool Table Simulation")
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        """Draw the ball on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        """Update ball position and apply friction."""
        self.x += self.vx
        self.y += self.vy

        # Apply friction
        self.vx *= (1 - FRICTION)
        self.vy *= (1 - FRICTION)

        # Bounce off walls
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.vx = -self.vx
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.vy = -self.vy

    def collide(self, other):
        """Handle collisions with another ball."""
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + other.radius:  # Collision detected
            angle = math.atan2(dy, dx)

            # Swap velocities realistically
            v1x, v1y = self.vx, self.vy
            v2x, v2y = other.vx, other.vy

            self.vx = v2x
            self.vy = v2y
            other.vx = v1x
            other.vy = v1y


def main():
    # Create balls
    ball1 = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_COLOR)
    ball2 = Ball(WIDTH // 2 + 50, HEIGHT // 2, BALL_RADIUS, BALL_COLOR)
    balls = [ball1, ball2]

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mx, my = pygame.mouse.get_pos()
                    for ball in balls:
                        dx = mx - ball.x
                        dy = my - ball.y
                        distance = math.hypot(dx, dy)
                        if distance < ball.radius:  # Clicked on a ball
                            ball.vx = dx * 0.1
                            ball.vy = dy * 0.1

        # Update ball positions
        for ball in balls:
            ball.update()

        # Handle collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].collide(balls[j])

        # Drawing
        screen.fill(TABLE_COLOR)
        for ball in balls:
            ball.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()
