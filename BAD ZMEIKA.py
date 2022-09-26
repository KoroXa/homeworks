# игра змейка
import pygame, time, random

pygame.init()

font_style = pygame.font.SysFont("comicsansms", 50)
score_font_style = pygame.font.SysFont("comicsansms", 25)
def draw_text(text, color):
	msg = font_style.render(text, True, color)
	dis.blit(msg, [WIDTH / 2, HEIGHT / 2])
BLUE = (0, 0, 255)
GREEN = (7, 155, 70)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
WIDTH = 800
HEIGHT = 600

score = 0
snake_length = 1
snake_list = []

def draw_snake(snake_block, snake_list):
	for i in snake_list:
		pygame.draw.rect(dis, BLUE, [i[0], i[1], snake_block, snake_block])
		
def draw_score(score):
	w = score_font_style.render("ОЧКИ: "+ str(score), True, YELLOW)
	dis.blit(w, [0, 0])
							

	

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
pygame.display.set_caption("ZMEIKA")
game_over = False
speed = 10
FPS = speed
clock = pygame.time.Clock()
x1 = 200
y1 = 150

snake_width = 10

x1_change = 0
y1_change = 0





food_x = round(random.randrange(0, WIDTH - snake_width) / 10.0) * 10.0
food_y = round(random.randrange(0, HEIGHT - snake_width) / 10.0) * 10.0
while not game_over:
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x1_change = -speed
				y1_change = 0
			elif event.key == pygame.K_d:
				x1_change = speed
				y1_change = 0
			elif event.key == pygame.K_w:
				x1_change = 0
				y1_change = -speed
			elif event.key == pygame.K_s:
				x1_change = 0
				y1_change = speed
				
	if x1 >= WIDTH or x1<0 or y1 >= HEIGHT or y1 <0 or score == -1:
		game_over = True
				
	for i in snake_list[:-1]:
		if i == snake_head:
			game_over = True
	x1 += x1_change 
	y1 += y1_change 
	dis.fill(GREEN) 
	#pygame.draw.rect(dis,BLUE, [x1, y1, snake_width, snake_width]) 
	snake_head = [] 
	snake_head.append(x1) 
	snake_head.append(y1) 
	snake_list.append(snake_head) 
	if len(snake_list) > snake_length:
		del(snake_list[0])
		
	draw_snake(snake_width, snake_list)	
	draw_score(score)
	pygame.draw.rect(dis, RED, [food_x, food_y, snake_width, snake_width])		#рисует прямоугольник на дис
	pygame.display.update()
	
	if x1 == food_x and y1 == food_y:
		
		food_x = round(random.randrange(0, WIDTH - snake_width) / 10.0) * 10.0
		food_y = round(random.randrange(0, HEIGHT - snake_width) / 10.0) * 10.0
		score += 1
		snake_length += 0
	
	clock.tick(FPS)
	
draw_text("Конец игры!", RED)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()
