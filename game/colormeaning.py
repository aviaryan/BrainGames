from game import boolgame
from utils.draw import RectangularButton
from utils.colors import Colors
from utils import maths


class ColorMeaningGame(boolgame.BoolGame, Colors):

	def __init__(self, width, height):

		self.colors = [ [255,0,0] , [255,255,255] , [0,255,0] , [255,255,0] ]
		self.colornames = ['red', 'white', 'green', 'yellow']

		boolgame.BoolGame.__init__(self, 'Color Meaning', width, height, description='Check if meaning of text on left is same as color of text on right', color = '#0B3526')

		self.leftBtn = RectangularButton('yellow', 1, self.width//2 - 120, self.description.y - 100, w = 120, h = 100, color = self.solarized, textcolor=self.red, textsize = 22)
		self.rightBtn = RectangularButton('white', 1, self.width//2 + 20, self.description.y - 100, w = 120, h = 100, color = self.solarized, textcolor=self.yellow, textsize = 22)


	def game_on_draw(self):
		self.window.clear()
		self.leftBtn.draw()
		self.rightBtn.draw()


	def addNew(self):

		self.syncKey = True

		self.answer = maths.weightedRandomIndex([0.6, 0.4]) # 0.6 for 0 i.e wrong answer
		leftid = maths.randint(0,3)
		leftnameid = maths.randint(0,3)

		if self.answer == 0:
			rightid_pdf = popList(leftid, 0.2) + [0.4] + popList(3-leftid, 0.2) # 0.4 chance left color = right color
			rightid = leftnameid
			while rightid == leftnameid:
				rightid = maths.weightedRandomIndex(rightid_pdf)
			rightnameid = maths.randint(0,3)
		else:
			rightid = leftnameid
			rightnameid_pdf = popList(leftid, 0.2) + [0.4] + popList(3-leftid, 0.2)
			rightnameid = maths.weightedRandomIndex(rightnameid_pdf)

		self.rightBtn.label.text = self.colornames[rightnameid]
		self.rightBtn.label.color = self.colors[rightid] + [255]
		self.leftBtn.label.text = self.colornames[leftnameid]
		self.leftBtn.label.color = self.colors[leftid] + [255]

		self.syncKey = False




def popList(size, data):
	lst = []
	for i in range(size):
		lst += [data]
	return lst