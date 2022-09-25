import pygame, random, time

BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
WIDTH = 700
HEIGHT = 400
FPS = 60

#def sleep():
	#global block_list, all_sprites_list
	#time.sleep(1)
	#block_list.add(block)
	#all_sprites_list.add(block)

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		
		self.left_boundary = 0		#боудери = грань
		self.right_boundary = 0
		self.top_boundary = 0
		self.bottom_boundary = 0
		
		self.change_x = 0
		self.change_y = 0
		
	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		
		if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
			self.change_x *= -1		# меняем напровление на противополож
			
		if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
			self.change_y *= -1		# меняем напровление на противополож
	
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

player = Block(RED, 5, 5)
all_sprites_list.add(player)

for i in range(50):
	block = Block(BLACK, 20, 15)
	block.rect.x = random.randint(0, WIDTH)
	block.rect.y = random.randint(0, HEIGHT)
	block.change_x = random.randrange(-4, 4)
	block.change_y = random.randrange(-4, 4)
	
	block.left_boundary = 0		#боудери = грань
	block.right_boundary = WIDTH
	block.top_boundary = 0
	block.bottom_boundary = HEIGHT
	
	block_list.add(block)
	all_sprites_list.add(block)
	
	

running = True
score = 0
k = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(WHITE)
	pos = pygame.mouse.get_pos()		#опр x and y мышки
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	blocks_hit_list = []
	if k < 200:
		k += 1
	else:
		blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	
	# if score == 50:
		# score = 0
		# block_hit_list = 0
		# for i in range(50):
			# block = Block(BLACK, 20, 15)
			# block.rect.x = random.randint(0, WIDTH)
			# block.rect.y = random.randint(0, HEIGHT)
			# block.change_x = random.randrange(-4, 4)
			# block.change_y = random.randrange(-4, 4)
			
			# block.left_boundary = 0		#боудери = грань
			# block.right_boundary = WIDTH
			# block.top_boundary = 0
			# block.bottom_boundary = HEIGHT
			
			# block_list.add(block)
			# all_sprites_list.add(block)
		
	if k >= 200:
		for block in blocks_hit_list:
			block = Block(BLACK, 20, 15)
			block.rect.x = pos[0]
			block.rect.y = pos[1]
			block.change_x = 1#random.randrange(-4, 4)
			block.change_y = 1#random.randrange(-4, 4)
				
			block.left_boundary = 0		#боудери = грань
			block.right_boundary = WIDTH
			block.top_boundary = 0
			block.bottom_boundary = HEIGHT
			block_list.add(block)
			all_sprites_list.add(block)
			all_sprites_list.update()
			score+= 1
			print(score)
	
	all_sprites_list.update()
	all_sprites_list.draw(screen)
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()
