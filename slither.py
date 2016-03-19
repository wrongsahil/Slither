import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)
black = (0, 0, 0)
snake_width = 15
snake_height = 15
apple_height = 15
apple_width = 15

gameDisplay = pygame.display.set_mode([1200, 700])
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()

def print_snake(snake_x, snake_y, snake_len):
	for i in range(0, len(snake_x)):
		pygame.draw.rect(gameDisplay, green, [snake_x[i], snake_y[i], snake_width, snake_height])

def snake_head_collision(x, y, snake_x, snake_y, direction):
	for i in range(0, len(snake_x)-3):
		'''if direction == 'up':
			if x >= snake_x[i] and x<= (snake_x[i]+snake_width) and y >= snake_y[i] and y<= (snake_y[i]+snake_height):
				return True
			elif(x+snake_width) >= snake_x[i] and (x+snake_width) <= (snake_x[i]+snake_width) and y >= snake_y[i] and y<= (snake_y[i]+snake_height):
				return True
		elif direction == 'down':
			if x >= snake_x[i] and x <= (snake_x[i] + snake_width) and (y + snake_height) >= snake_y[i] and (y + snake_height) <= (snake_y[i] + snake_height):
				return True
			elif (x + snake_width) >= snake_x[i] and (x + snake_width) <= (snake_x[i] + snake_width) and (y + snake_height) >= snake_y[i] and (y + snake_height) <= (snake_y[i] + snake_height):
				return True
		elif direction == 'right':
			if (x + snake_width) >= snake_x[i] and (x + snake_width)<= (snake_x[i]+snake_width) and y >= snake_y[i] and y<= (snake_y[i]+snake_height):
				return True
			elif(x+snake_width) >= snake_x[i] and (x+snake_width) <= (snake_x[i]+snake_width) and (y + snake_height) >= snake_y[i] and (y + snake_height)<= (snake_y[i]+snake_height):
				return True
		elif direction == 'left':
			if x >= snake_x[i] and x<= (snake_x[i]+snake_width) and y >= snake_y[i] and y<= (snake_y[i]+snake_height):
				return True
			elif x >= snake_x[i] and x <= (snake_x[i]+snake_width) and (y + snake_height) >= snake_y[i] and (y + snake_height)<= (snake_y[i]+snake_height):
				return True
		'''
		if x == snake_x[i] and y == snake_y[i]:
			return True

	return False

def get_apple():
	apple_x = random.randrange(0, 1200-apple_width)
	apple_y = random.randrange(0, 700-apple_height)
	pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, apple_width, apple_height])
	return apple_x, apple_y

def gameloop():

	gameExit = False
	x = 600
	y = 400
	change_x = 15
	change_y = 0
	snake_len = 10
	snake_x = []
	snake_y = []
	direction = 'right'
	i=1
	apple_x, apple_y = get_apple()

	while not gameExit:

		print i
		i+=1
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

		if x+change_x>=0 and (x+change_x+snake_width)<=1200:
			x += change_x
		else:
			gameExit = True
		if y+change_y>=0 and+ (y+change_y+snake_height)<=700:
			y += change_y
		else:
			gameExit = True

		if (apple_x >= x and apple_x <= (x + snake_width) and apple_y >= y and apple_y <= (y + snake_height)):
			apple_x, apple_y = get_apple()
			snake_len += 1
		elif (apple_x + apple_width >= x and apple_x + apple_width <= (x + snake_width) and apple_y + apple_height >= y and apple_y + apple_height <= (y + snake_height)):
			apple_x, apple_y = get_apple()
			snake_len += 1
		elif (apple_x + apple_width >= x and apple_x + apple_width <= (x + snake_width) and apple_y >= y and apple_y <= (y + snake_height)):
			apple_x, apple_y = get_apple()
			snake_len += 1
		elif (apple_x >= x and apple_x <= (x + snake_width) and apple_y + apple_height >= y and apple_y + apple_height <= (y + snake_height)):
			apple_x, apple_y = get_apple()
			snake_len += 1

		snake_x.append(x)
		snake_y.append(y)

		if snake_len < len(snake_x):
			del snake_x[0]
			del snake_y[0]

		gameExit = snake_head_collision(x, y, snake_x, snake_y, direction)

		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, apple_width, apple_height])
		#pygame.draw.rect(gameDisplay, green, [x, y, snake_width, snake_height])
		print_snake(snake_x, snake_y, snake_len)
		pygame.display.update()
		clock.tick(30)

	pygame.quit()
	quit()

gameloop()