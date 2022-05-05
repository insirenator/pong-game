import pygame
from components import Paddle
from components import Ball

class Pong:
	def __init__(self):
		self.WIDTH,self.HEIGHT = 600,500
		self.VEL = 5
		self.SCREEN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
		
		pygame.display.set_caption("PONG!")

		self.paddle_L = Paddle(10,150,(0,0))
		self.paddle_R = Paddle(10,150,(self.WIDTH-11,0))
		self.ball = Ball(15,(300,250), 10)

		#Translation Factors for ball motion
		self.tf_x = 1
		self.tf_y = 1

	def handle_movement(self, key_pressed):
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
		if ball.x < 0 or ball.x > self.WIDTH :
			return True
		elif ball.y < 0 or ball.y > self.HEIGHT :
			return True
		else:
			return False



	def translate_ball(self,ball):
		if ball.y + ball.height + self.tf_y > self.HEIGHT:
			self.tf_y = -(self.tf_y)
		if ball.y + self.tf_y < 0 :
			self.tf_y = -(self.tf_y)

		if ball.x + ball.width + self.tf_x > self.WIDTH and self.paddle_R.y < ball.y < self.paddle_R.y + self.paddle_R.height:
			self.tf_x = -(self.tf_x)
		if ball.x + self.tf_x < 0 and self.paddle_L.y < ball.y < self.paddle_L.y + self.paddle_L.height:
			self.tf_x = -(self.tf_x)



		ball.x += self.tf_x
		ball.y += self.tf_y


	def run_game(self):
		clock = pygame.time.Clock()
		FPS = 120
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			key_pressed = pygame.key.get_pressed()
			self.handle_movement(key_pressed)
			self.SCREEN.fill((0,0,0))
			self.paddle_L.draw(self.SCREEN)
			self.paddle_R.draw(self.SCREEN)
			self.translate_ball(self.ball)
			self.ball.draw(self.SCREEN)
			pygame.display.update()

			if self.ball_outbound(self.ball):
				run = False


		pygame.quit()		