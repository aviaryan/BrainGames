from game import boolgame
import pyglet
import random
from utils import maths


class MathGame(boolgame.BoolGame):

	def __init__(self, width, height):

		super().__init__('Math Game', width, height, description='Check if the expression is true or not')

		self.lblExp = pyglet.text.Label('abc', font_size=20, x = self.width//2, y = self.description.y - 100, anchor_x = 'center', anchor_y = 'center')
		self.components += [self.lblExp]
		self.lblExp.draw()


	def addNew(self):

		self.syncKey = True

		self.lblExp.text = 'new text ' + str( random.random() )
		self.lblExp.draw()
		self.answer = False

		self.syncKey = False