
class QuesGame():

	def __init__(self, numQuestions=10):
		self.numQuestions = numQuestions

	def endTime(self):
		pass

	def submit(self, ans):
		if ans == self.answer:
			self.updateScore(self.positive)
		else:
			self.updateScore(self.negative)
		self.showAnswer(ans == self.answer)


	def showAnswer(self, status):
		pass

	def undo_showAnswer(self, dt):
		pass