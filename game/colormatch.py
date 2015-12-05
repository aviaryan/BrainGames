from game import boolgame
from utils import draw, motion
import random


class ColorMatchGame(boolgame.BoolGame):

	def __init__(self, width, height):

		self.colors = [ [255,0,0] , [0,255,0] , [0,0,255] , [255,255,0] ]
		self.shapes = ['circle', 'square', 'hexagon', 'triangle']

		super().__init__('Color Match', width, height, description='Check if previous color is same as current one.')

		self.curshape = draw.circle(self.width//2 - 75, 300, 75, filled=True, color=self.colors[0])
		self.curshape.draw()
		self.components += [self.curshape]
		self.previous = 0
		self.window.push_handlers(on_draw = self.pyglet_on_draw)


	def pyglet_on_draw(self):
		'''
		Default on_draw event for the game
		'''
		self.window.clear()
		self.curshape.draw()


	def addNew(self):

		self.syncKey = True

		col = random.randint(0, len(self.colors)-1)
		shape = random.randint(0, len(self.shapes)-1)
		cshape = self.shapes[shape]
		self.answer = True if (col == self.previous) else False
		self.previous = col

		self.curshape.figure.delete()
		# motion.wait(1000)
		if cshape == 'square':
			self.curshape = draw.square(self.width//2 - 75, 300, 150, filled=True, color=self.colors[col])
		elif cshape == 'hexagon':
			self.curshape = draw.hexagon(self.width//2 - 75, 300, 75, filled=True, color=self.colors[col])
		elif cshape == 'triangle':
			self.curshape = draw.triangle(self.width//2 - 75, 300, 150, filled=True, color=self.colors[col])
		else:
			self.curshape = draw.circle(self.width//2 - 75, 300, 75, filled=True, color=self.colors[col])
		self.components.pop()
		self.curshape.draw()
		self.components += [self.curshape]

		self.syncKey = False
		return