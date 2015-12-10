import json
import os
from datetime import date


defaultSettings = {
	'positive': 10,
	'negative': -20,
	'gameTime': 45
}
fname = 'braingames.json'


def loadSettings():
	'''
	loads the settings.
	creates the settings file if needed
	'''
	if not os.path.isfile(fname):
		saveSettings(defaultSettings)
		config = defaultSettings
	else:
		config = json.loads( open(fname, 'r').read() )
	return config


def saveSettings(config):
	open(fname, 'w').write(json.dumps(config, indent=4, sort_keys=True))


def saveScore(gameid, score):
	'''
	saves score for a game
	'''
	if score == '':
		return
	today = date.today()
	config = loadSettings()
	gameid = '_' + gameid
	if gameid not in config:
		config[gameid] = {}
	if 'scores' not in config[gameid]:
		config[gameid]['scores'] = {}
	dateStr = str(today)
	if dateStr in config[gameid]['scores']:
		score = max(config[gameid]['scores'][dateStr], score)
	config[gameid]['scores'][dateStr] = score
	saveSettings(config)


def getHighScore(gameid):
	'''
	get highest score in a game
	'''
	gconfig = loadGameSettings(gameid)
	scores = gconfig.get('scores', {})
	if len(scores) == 0:
		return 0
	return max( scores[i] for i in scores )


def loadGameSettings(gameid):
	'''
	loads settings for a game, if setting is not present, return default
	'''
	config = loadSettings()
	gameid = '_' + gameid
	if gameid not in config:
		return {}
	else:
		return config[gameid]



if __name__ == '__main__':
	config = loadSettings()
	print(config)
	saveScore('colormatch', 49)
	saveScore('scrabble', 54)