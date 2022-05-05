'''
Pong Game in Python using Pygame Module
Created by : Shakeeb Arsalaan
Dated : 05-04-2022
'''

import pygame
from random import choice

from components import Paddle
from components import Ball
from components import GAME_OVER_IMG

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)


class Pong:
	'''Main Game Class'''
	def __init__(self):
		pygame.init()
		self.WIDTH,self.HEIGHT = 800,600
		self.VEL = 5
		self.SCREEN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
		
		pygame.display.set_caption("PONG!")

		self.paddle_L = Paddle(10,150,(0,0))
		self.paddle_R = Paddle(10,150,(self.WIDTH-11,0))
		self.ball = Ball(15,(self.WIDTH/2, self.HEIGHT/2), 10)

		self.center_border = pygame.Rect(self.WIDTH/2 - 1, 0, 2, self.HEIGHT)

		#Paddle Hits
		self.left_hits = 0
		self.right_hits = 0

		#Text Objects
		self.FONT = pygame.font.Font('freesansbold.ttf',28)
		self.right_score = self.FONT.render(str(self.right_hits), True, WHITE, BLACK)
		self.left_score = self.FONT.render(str(self.left_hits), True, WHITE, BLACK) 

		self.l_text_rect = self.left_score.get_rect()
		self.l_text_rect.center = ((self.WIDTH/4)*3, 20)
		self.r_text_rect = self.right_score.get_rect()
		self.r_text_rect.center = (self.WIDTH/4, 20)

		#Translation Factors for ball motion
		self.tf_x = choice([1,-1])
		self.tf_y = choice([1,-1])

	def display_score(self):
		'''Display the scores of the players'''
		self.right_score = self.FONT.render(str(self.right_hits), True, WHITE, BLACK)
		self.left_score = self.FONT.render(str(self.left_hits), True, WHITE, BLACK)
		self.SCREEN.blit(self.left_score, self.l_text_rect)
		self.SCREEN.blit(self.right_score, self.r_text_rect)

	def draw_center_border(self):
		pygame.draw.rect(self.SCREEN, WHITE, self.center_border)

	def handle_movement(self, key_pressed):
		'''Respond to the keys pressed'''
		#Left Paddle
		if key_pressed[pygame.K_w]:
			self.paddle_L.move_up(self.VEL)
		if key_pressed[pygame.K_s]:
			self.paddle_L.move_down(self.VEL, self.HEIGHT)

		#Right Paddle
		if key_pressed[pygame.K_UP]:
			self.paddle_R.move_up(self.VEL)
		if key_pressed[pygame.K_DOWN]:
			self.paddle_R.move_down(self.VEL, self.HEIGHT)

	def ball_outbound(self, ball):
		'''Check if ball is out of bound'''
		if ball.x < 0 or ball.x > self.WIDTH :
			return True
		elif ball.y < 0 or ball.y > self.HEIGHT :
			return True
		else:
			return False

	def translate_ball(self,ball):
		'''Control the motion of the ball'''
		if ball.y + ball.height + self.tf_y > self.HEIGHT:
			self.tf_y = -(self.tf_y)
		if ball.y + self.tf_y < 0 :
			self.tf_y = -(self.tf_y)

		if ball.x + ball.width + self.tf_x > self.WIDTH and self.paddle_R.y < ball.y < self.paddle_R.y + self.paddle_R.height:
			self.tf_x = -(self.tf_x)
			self.left_hits += 1 # Update Left Hits
		if ball.x + self.tf_x < 0 and self.paddle_L.y < ball.y < self.paddle_L.y + self.paddle_L.height:
			self.tf_x = -(self.tf_x)
			self.right_hits += 1 # Update Right Hits


		ball.x += self.tf_x
		ball.y += self.tf_y


	def run_game(self):
		'''Game Driver'''
		clock = pygame.time.Clock()
		FPS = 120

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.quit()

			key_pressed = pygame.key.get_pressed()
			self.handle_movement(key_pressed)
			self.SCREEN.fill(BLACK)
			self.draw_center_border()
			self.paddle_L.draw(self.SCREEN)
			self.paddle_R.draw(self.SCREEN)
			self.translate_ball(self.ball)
			self.ball.draw(self.SCREEN)
			self.display_score()
			pygame.display.update()

			if self.ball_outbound(self.ball):
				run = False

		self.SCREEN.blit(GAME_OVER_IMG,(self.WIDTH/2-200,self.HEIGHT/2-60))
		pygame.display.update()

		pygame.event.clear()
		while True:
			event = pygame.event.wait()
			if event.type == pygame.QUIT:
				pygame.quit()		