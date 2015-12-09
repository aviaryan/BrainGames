from game import colormatch
from game import mathgame
from game import calcgame
from game import scrabble
from game import colormeaning
from features import settings

# newgame = boolgame.BoolGame('My game', width=700, height=500, description='test this thing')
# newgame.show()
# newgame.start()

# newgame = colormatch.ColorMatchGame(700, 500)
# newgame = mathgame.MathGame(600, 500)
# newgame = subjectivegame.SubjectiveGame('My game', 700, 500, description='test')
# newgame = calcgame.CalcGame(600, 500)
newgame = scrabble.Scrabble(700, 500)
# newgame = colormeaning.ColorMeaningGame(700, 500)

x = newgame.start()

settings.saveScore(x[0], x[1])