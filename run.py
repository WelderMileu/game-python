import pygame
from pygame.locals import *
import os
import time

class run:
	def __init__ (self):
		self.screen_width = 600
		self.screen_height = 570
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.clock = pygame.time.Clock()
		self.move_persona = 0

		# images
		self.image1 = pygame.image.load(os.path.join('images', 'pessona1.png'))
		self.image2 = pygame.image.load(os.path.join('images', 'pessona2.png'))
		self.image3 = pygame.image.load(os.path.join('images', 'pessona3.png'))
		self.image4 = pygame.image.load(os.path.join('images', 'pessona4.png'))
		self.bg_image = pygame.image.load(os.path.join('images', 'image_bg.jpg')).convert() 
		self.movbg = 0

	def loop(self):		
		# position and image.
		x = (self.screen_width * 0.45)
		y = (self.screen_height * 0.6)

		self.screen.fill((255,255,255))
		self.screen.blit(self.bg_image , (self.movbg, -180))
		self.screen.blit(self.image1, (x, y))

		pygame.display.flip()
		pygame.display.update()
		pygame.display.set_caption("run and pocket")
		pygame.display.init()

		def render():
			pygame.display.update()

		# loop and aplication
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			events = pygame.key.get_pressed()
			image_size = "-{}".format(self.bg_image.get_rect().size[0])
			
			if events[K_LEFT]:
				self.movbg = self.movbg + 10
				self.screen.blit(self.bg_image , (self.movbg, -180))
				self.move_persona = self.move_persona + 1

				if self.move_persona == 3:
					self.move_persona = 0

				move = [self.image1, self.image2, self.image3, self.image4]
				
				if self.movbg == 10:
					self.movbg = self.movbg - 10
					index = 1	
					move[index] = pygame.transform.flip(move[index], True, False)
					self.screen.blit(move[index], (x, y))

				else:
					self.clock.tick(25)
					self.screen.blit(self.bg_image , (self.movbg, -180))				
					move[self.move_persona] = pygame.transform.flip(move[self.move_persona], True, False)

					self.screen.blit(move[self.move_persona], (x, y))

			if events[K_RIGHT]:
				self.movbg -= 10
				self.move_persona = self.move_persona + 1

				if self.move_persona == 3:
					self.move_persona = 0

				move = [self.image1, self.image2, self.image3, self.image4]
				
				self.clock.tick(25)
				self.screen.blit(self.bg_image , (self.movbg, -180))				
				self.screen.blit(move[self.move_persona], (x, y))

			if int(image_size) == self.movbg-580:
				self.movbg = 10

			if self.movbg == 10:
				self.movbg = self.movbg - 10
				

			render()

			self.clock.tick(20)


run = run()
run.loop()