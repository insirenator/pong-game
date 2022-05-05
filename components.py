'''
Components for the Pong Game 
i.e. Paddle and Ball
'''

import pygame
import os

PADDLE_IMG = pygame.image.load(os.path.join("assets","paddle.png"))
BALL_IMG = pygame.image.load(os.path.join("assets","ball.png"))
GAME_OVER_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets","game_over.png")),(400,60))

class Paddle:
	'''Represents the game paddle'''
	def __init__(self, width, height, coords):
		self.img = pygame.transform.scale(PADDLE_IMG,(width, height))
		self.width = width
		self.height = height
		self.x, self.y = coords

	def draw(self, SCREEN):
		'''Draw paddle on the screen'''
		SCREEN.blit(self.img,(self.x, self.y))

	def move_up(self, VEL):
		'''Move the paddle up'''
		if self.y - VEL > 0 :
			self.y -= VEL

	def move_down(self, VEL, HEIGHT):
		'''Move the paddle down'''
		if self.y + VEL + self.height < HEIGHT :
			self.y += VEL

class Ball:
	'''Represents the Ball'''
	def __init__(self, diameter, coords, velocity):
		self.img = pygame.transform.scale(BALL_IMG,(diameter,diameter))
		self.VEL = velocity
		self.width = diameter
		self.height = diameter
		self.x, self.y = coords

	def draw(self, SCREEN):
		'''Draw the ball on the screen'''
		SCREEN.blit(self.img,(self.x, self.y))