import pygame
import random
import sys

# 初始化
pygame.init()

# 游戏常量
WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20
SPEED = 10

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (1, 0)  # 初始向右移动
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx*GRID_SIZE) % WIDTH, (head_y + dy*GRID_SIZE) % HEIGHT)
        
        if new_head in self.body:
            game_over()
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        while True:
            x = random.randint(0, (WIDTH-GRID_SIZE)//GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (HEIGHT-GRID_SIZE)//GRID_SIZE) * GRID_SIZE
            if (x, y) not in snake.body:
                return (x, y)

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def game_over():
    font = pygame.font.SysFont('arial', 50)
    text = font.render(f'Game Over! Score: {len(snake.body)}', True, RED)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# 游戏对象
snake = Snake()
food = Food()

clock = pygame.time.Clock()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)
            elif event.key == pygame.K_SPACE:  # 按空格键重新开始
                snake = Snake()
                food = Food()

    # 检测是否吃到食物
    if snake.body[0] == food.position:
        snake.grow = True
        food = Food()

    snake.move()

    # 绘制画面
    screen.fill(WHITE)
    draw_grid()
    
    # 绘制蛇
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE-1, GRID_SIZE-1))
    
    # 绘制食物
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], GRID_SIZE-1, GRID_SIZE-1))

    pygame.display.update()
    clock.tick(SPEED)