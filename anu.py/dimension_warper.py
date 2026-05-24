import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 40
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dimension Warper: Jacobian Mayhem")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
PURPLE = (180, 50, 180)

# Player setup
player = [5, 5]
score = 0
energy = 100

# Enemy setup (simple patrol)
enemies = [[10, 10], [12, 8]]
enemy_dir = [1, -1]

# Goal portal
goal = [14, 14]

# Jacobian calculation (simple finite difference)
def jacobian(u_func, v_func, x=1.0, y=1.0):
    h = 0.01
    def f(expr, x, y):
        return eval(expr)
    du_dx = (f(u_func, x+h, y) - f(u_func, x, y)) / h
    du_dy = (f(u_func, x, y+h) - f(u_func, x, y)) / h
    dv_dx = (f(v_func, x+h, y) - f(v_func, x, y)) / h
    dv_dy = (f(v_func, x, y+h) - f(v_func, x, y)) / h
    return du_dx * dv_dy - du_dy * dv_dx

# Draw grid, player, enemies, goal
def draw():
    screen.fill(WHITE)
    for i in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (i,0), (i,HEIGHT))
    for j in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0,j), (WIDTH,j))

    # Player
    pygame.draw.rect(screen, BLUE, (player[0]*GRID_SIZE, player[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
    # Enemies
    for e in enemies:
        pygame.draw.rect(screen, RED, (e[0]*GRID_SIZE, e[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
    # Goal
    pygame.draw.rect(screen, GREEN, (goal[0]*GRID_SIZE, goal[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # HUD
    font = pygame.font.SysFont(None, 24)
    hud = font.render(f"Score: {score}  Energy: {energy}", True, (0,0,0))
    screen.blit(hud, (10,10))

    pygame.display.flip()

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: player[1] -= 1
    if keys[pygame.K_DOWN]: player[1] += 1
    if keys[pygame.K_LEFT]: player[0] -= 1
    if keys[pygame.K_RIGHT]: player[0] += 1

    # Enemy patrol
    for i, e in enumerate(enemies):
        e[0] += enemy_dir[i]
        if e[0] <= 0 or e[0] >= COLS-1:
            enemy_dir[i] *= -1

    # Collision check
    for e in enemies:
        if player == e:
            score -= 25
            print("⚠ Hit enemy! -25 points")

    # Goal check
    if player == goal:
        score += 100
        print("🏆 Goal reached! +100 points")
        running = False

    draw()

pygame.quit()
sys.exit()
