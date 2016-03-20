import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 155)
green = (0, 155, 0)
black = (0, 0, 0)
yellow = (255, 255, 100)

snake_width = 15
snake_height = 15
apple_height = 15
apple_width = 15

gameDisplay = pygame.display.set_mode([1200, 690])
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()

apple = pygame.image.load("apple.png")
head = pygame.image.load("head.png")
tail = pygame.image.load("tail.png")

font_large = pygame.font.SysFont(None, 100)
font_medium = pygame.font.SysFont(None, 40)
font = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None,30)

def start_menu(gameExit):
	font_slither = pygame.font.SysFont(None, 150)
	text1 = font_slither.render("Slither", True, green)
	gameDisplay.fill(white)
	gameDisplay.blit(text1, [470,240])
	text2 = font_medium.render("Press 'c' to play, 'ESC' to exit & 'p' to pause", True, black)
	gameDisplay.blit(text2, [370, 370])
	text2 = font_medium.render("Eat Apples and do not hit the walls or yourself", True, red)
	gameDisplay.blit(text2, [340, 420])
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				return gameExit
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					return gameExit
				elif event.key == pygame.K_ESCAPE:
					gameExit = True
					return gameExit

def print_score(score):
	text1 = font_large.render("Score", True, blue)
	gameDisplay.blit(text1, [970, 100])
	text2 = font.render(str(score), True, green)
	gameDisplay.blit(text2, [1050, 200])
	text3 = font.render("SLITHER", True, green)
	gameDisplay.blit(text3, [970, 500])
	text4 = font_small.render("Press 'p' to pause", True, red)
	gameDisplay.blit(text4, [970, 550])
	text5 = font_small.render("Press 'ESC' to quit", True, red)
	gameDisplay.blit(text5, [970, 580])
	pygame.display.update()




def game_over(gameExit):
	text1 = font_large.render("Game Over", True, red)
	gameDisplay.blit(text1, [300, 250])
	text2 = font_medium.render("Press 'c' to PLAY AGAIN and 'q' to quit", True, black)
	gameDisplay.blit(text2, [240 ,330])
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameExit = True
					return gameExit
				elif event.key == pygame.K_c:
					return gameExit
			elif event.type == pygame.QUIT:
				gameExit = True
				return gameExit

def game_pause(gameExit):
	text1 = font_large.render("Paused", True, red)
	gameDisplay.blit(text1, [330, 250])
	text2 = font_medium.render("Press 'c' to resume and 'q' to quit", True, black)
	gameDisplay.blit(text2, [240 ,330])
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameExit = True
					return gameExit
				elif event.key == pygame.K_c:
					return gameExit
			elif event.type == pygame.QUIT:
				gameExit = True
				return gameExit

def print_snake(snake_x, snake_y, snake_len, direction):
	for i in range(0, len(snake_x)-1):
		pygame.draw.rect(gameDisplay, green, [snake_x[i], snake_y[i], snake_width, snake_height])

	if direction == 'up':
		head_rotate = head
		#tail_rotate = pygame.transform.rotate(tail, 180)
	elif direction == 'down':
		head_rotate = pygame.transform.rotate(head, 180)
		#tail_rotate = tail
	elif direction == 'right':
		head_rotate = pygame.transform.rotate(head,270)
		#tail_rotate = pygame.transform.rotate(tail, 90)
	elif direction == 'left':
		head_rotate = pygame.transform.rotate(head, 90)
		#tail_rotate = pygame.transform.rotate(tail, 270)

	gameDisplay.blit(head_rotate, [snake_x[-1], snake_y[-1]])
	#gameDisplay.blit(tail_rotate, [snake_x[0], snake_y[0]])

def snake_head_collision(x, y, snake_x, snake_y, direction, gameExit):
	for i in range(0, len(snake_x)-1):
		if x == snake_x[i] and y == snake_y[i]:
			return True
	if gameExit == False:
		return False

	return True

def get_apple(snake_x, snake_y):
	coincide = True

	while coincide:
		apple_x = random.randrange(15, 915-apple_width)
		apple_y = random.randrange(15, 675-apple_height)
		#pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, apple_width, apple_height])
		coincide = False

		for i in range(0, len(snake_x)):
			if (apple_x >= snake_x[i] and apple_x <= (snake_x[i] + snake_width) and apple_y >= snake_y[i] and apple_y <= (snake_y[i] + snake_height)):
				apple_x, apple_y = get_apple()
				coincide = True
				break
			elif (apple_x + apple_width >= snake_x[i] and apple_x + apple_width <= (snake_x[i] + snake_width) and apple_y + apple_height >= snake_y[i] and apple_y + apple_height <= (snake_y[i] + snake_height)):
				apple_x, apple_y = get_apple()
				coincide = True
			elif (apple_x + apple_width >= snake_x[i] and apple_x + apple_width <= (snake_x[i] + snake_width) and apple_y >= snake_y[i] and apple_y <= (snake_y[i] + snake_height)):
				apple_x, apple_y = get_apple()
				coincide = True
			elif (apple_x >= snake_x[i] and apple_x <= (snake_x[i] + snake_width) and apple_y + apple_height >= snake_y[i] and apple_y + apple_height <= (snake_y[i] + snake_height)):
				apple_x, apple_y = get_apple()
				coincide = True
	
	return apple_x, apple_y

def gameloop():

	gameExit = False
	gameOver = False
	gamePause = False
	x = 300
	y = 300
	change_x = 15
	change_y = 0
	snake_len = 1
	snake_x = []
	snake_y = []
	direction = 'right'
	score = 0
	#i=1

	gameExit = start_menu(gameExit)

	if gameExit == True:
		pygame.quit()
		quit()

	apple_x, apple_y = get_apple(snake_x, snake_y)

	while not gameExit:

		#print i
		#i+=1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and direction != 'down':
					change_x = 0
					change_y = -15
					direction = 'up'
				elif event.key == pygame.K_DOWN and direction != 'up':
					change_x = 0
					change_y = 15
					direction = 'down'
				elif event.key == pygame.K_RIGHT and direction != 'left':
					change_y = 0
					change_x = 15
					direction = 'right'
				elif event.key == pygame.K_LEFT and direction != 'right':
					change_y = 0
					change_x = -15
					direction = 'left'
				elif event.key == pygame.K_ESCAPE:
					gameExit = True
					#gamePause = True
				elif event.key == pygame.K_p:
					gamePause = True

		if gamePause == True:
			gameExit = game_pause(gameExit)
			if gameExit == True:
				pygame.quit()
				quit()
			gamePause = False

		if x+change_x>=15 and (x+change_x+snake_width)<=915:
			x += change_x
		else:
			#gameExit = True
			gameOver = True
		if y+change_y>=15 and+ (y+change_y+snake_height)<=675:
			y += change_y
		else:
			#gameExit = True
			gameOver = True

		if gameOver == True:
			gameExit = game_over(gameExit)
			if gameExit == True:
				pygame.quit()
				quit()
			gameloop()


		if (apple_x >= x and apple_x <= (x + snake_width) and apple_y >= y and apple_y <= (y + snake_height)):
			apple_x, apple_y = get_apple(snake_x, snake_y)
			snake_len += 1
			score += 1
		elif (apple_x + apple_width >= x and apple_x + apple_width <= (x + snake_width) and apple_y + apple_height >= y and apple_y + apple_height <= (y + snake_height)):
			apple_x, apple_y = get_apple(snake_x, snake_y)
			snake_len += 1
			score += 1
		elif (apple_x + apple_width >= x and apple_x + apple_width <= (x + snake_width) and apple_y >= y and apple_y <= (y + snake_height)):
			apple_x, apple_y = get_apple(snake_x, snake_y)
			snake_len += 1
			score += 1
		elif (apple_x >= x and apple_x <= (x + snake_width) and apple_y + apple_height >= y and apple_y + apple_height <= (y + snake_height)):
			apple_x, apple_y = get_apple(snake_x, snake_y)
			snake_len += 1
			score += 1

		snake_x.append(x)
		snake_y.append(y)

		if snake_len < len(snake_x):
			del snake_x[0]
			del snake_y[0]

		gameExit = snake_head_collision(x, y, snake_x, snake_y, direction, gameExit)

		gameDisplay.fill(white)

		pygame.draw.rect(gameDisplay,black, [0, 0, 930, 15])
		pygame.draw.rect(gameDisplay, black, [915, 0, 15, 690])
		pygame.draw.rect(gameDisplay, black, [0, 0, 15, 690])
		pygame.draw.rect(gameDisplay, black, [0, 675, 930, 15])

		pygame.draw.rect(gameDisplay, yellow, [930, 0, 270, 690])
		pygame.draw.rect(gameDisplay, black, [930, 0, 270, 15])
		pygame.draw.rect(gameDisplay, black, [1185, 0, 15, 690])
		pygame.draw.rect(gameDisplay, black, [930, 675, 270, 15])

		print_score(score)

		#pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, apple_width, apple_height])
		gameDisplay.blit(apple, [apple_x, apple_y, apple_width, apple_height])
		#pygame.draw.rect(gameDisplay, green, [x, y, snake_width, snake_height])
		print_snake(snake_x, snake_y, snake_len, direction)
		pygame.display.update()
		clock.tick(25)

	pygame.quit()
	quit()

gameloop()