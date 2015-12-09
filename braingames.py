from game import colormatch
from game import mathgame
from game import calcgame
from game import scrabble
from game import colormeaning
from features import settings, gameover

# newgame = boolgame.BoolGame('My game', width=700, height=500, description='test this thing')
# newgame.show()
# newgame.start()

# newgame = colormatch.ColorMatchGame()
# newgame = mathgame.MathGame()
# newgame = calcgame.CalcGame()
#newgame = scrabble.Scrabble()
newgame = colormeaning.ColorMeaningGame()

x = newgame.start()

settings.saveScore(x[0], x[1])

n = gameover.GameOver(x[0], x[1])
x = n.start()

print(x)