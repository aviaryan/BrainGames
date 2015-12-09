from game import boolgame
from utils import draw, maths


class ColorMatchGame(boolgame.BoolGame):

	def __init__(self, width=700, height=500):

		self.colors = [ [255,0,0] , [0,255,0] , [0,0,255] , [255,255,0] ]
		self.shapes = ['circle', 'square', 'hexagon', 'triangle']

		super().__init__('Color Match', width, height, description='Check if previous color is same as current one.', color = '#0B3526')

		self.gameid = 'colormatch'
		self.curshape = draw.circle(self.width//2 - 75, 300, 75, filled=True, color=self.colors[0])
		self.curshape.draw()
		self.previous = 0
		self.previous_shape = 0


	def game_on_draw(self):
		'''
		Default on_draw event for the game
		'''
		self.window.clear()
		self.curshape.draw()


	def addNew(self):

		self.syncKey = True

		self.answer = maths.weightedRandomIndex([0.65, 0.35]) # 0.65 for 0 i.e wrong answer

		if self.answer == 1:
			col = self.previous
			shape = self.previous_shape
			while shape == self.previous_shape:
				shape = maths.randint(0, 3)
		else:
			col = self.previous
			while col == self.previous:
				col = maths.randint(0, 3)
			shape = maths.randint(0, 3)

		cshape = self.shapes[shape]

		self.previous = col
		self.previous_shape = shape
		self.curshape.figure.delete()

		if cshape == 'square':
			self.curshape = draw.square(self.width//2 - 75, 300, 150, filled=True, color=self.colors[col])
		elif cshape == 'hexagon':
			self.curshape = draw.hexagon(self.width//2 - 75, 300, 75, filled=True, color=self.colors[col])
		elif cshape == 'triangle':
			self.curshape = draw.triangle(self.width//2 - 75, 300, 150, filled=True, color=self.colors[col])
		else:
			self.curshape = draw.circle(self.width//2 - 75, 300, 75, filled=True, color=self.colors[col])
		self.curshape.draw()

		self.syncKey = False