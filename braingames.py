from game import colormatch
from game import mathgame
from game import subjectivegame
from game import calcgame
from game import choicegame


# newgame = boolgame.BoolGame('My game', width=700, height=500, description='test this thing')
# newgame.show()
# newgame.start()

# newgame = colormatch.ColorMatchGame(700, 500)
# newgame = mathgame.MathGame(600, 500)
# newgame = subjectivegame.SubjectiveGame('My game', 700, 500, description='test')
# newgame = calcgame.CalcGame(600, 500)
newgame = choicegame.ChoiceGame('asdaf', 700, 500)

newgame.start()