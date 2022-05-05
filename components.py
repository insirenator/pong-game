import pygame
import os

PADDLE_IMG = pygame.image.load(os.path.join("assets","paddle.png"))
BALL_IMG = pygame.image.load(os.path.join("assets","ball.png"))

class Paddle:
	def __init__(self, width, height, coords):
		self.img = pygame.transform.scale(PADDLE_IMG,(width, height))
		self.width = width
		self.height = height
		self.x, self.y = coords

	def draw(self, SCREEN):
		SCREEN.blit(self.img,(self.x, self.y))

	def move_up(self, VEL):
		if self.y - VEL > 0 :
			self.y -= VEL

	def move_down(self, VEL, HEIGHT):
		if self.y + VEL + self.height < HEIGHT :
			self.y += VEL

class Ball:
	def __init__(self, diameter, coords, velocity):
		self.img = pygame.transform.scale(BALL_IMG,(diameter,diameter))
		self.VEL = velocity
		self.width = diameter
		self.height = diameter
		self.x, self.y = coords

	def draw(self, SCREEN):
		SCREEN.blit(self.img,(self.x, self.y))