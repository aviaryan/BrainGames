from math import *
import random


def genStatement():
	'''
	Returns a boolean maths statement
	'''
	operators = ['+', '-', '*', '/', '^']
	operators_pdf = [0.33, 0.20, 0.27, 0.15, 0.05]
	print( operators[weightedRandomIndex(operators_pdf)] )
	numL = -10
	numH = 100
	LHSize = random.randint(1, 3)



def weightedRandomRange(pdf, ranges):
	'''
	get Weighted Random for a range
	Example - 
	pdf = [ (0,0.2) , (1,0.8) ]
	ranges = [ (1,2) , (2,3) ]
	Here number returned between 2 and 3 probability is 0.8
	'''
	r = weightedRandom(pdf)
	num = (ranges[r][1] - ranges[r][0]) * random.random()
	return ranges[r][0] + num


def weightedRandom(pdf):
	'''
	Weighted random
	http://stackoverflow.com/a/4266278/2295672
	'''
	# pdf = [(1, 0.1), (2, 0.05), (3, 0.05), (4, 0.2), (5, 0.4), (6, 0.2)]
	cdf = [(i, sum(p for j,p in pdf if j < i)) for i,_ in pdf]
	R = max(i for r in [random.random()] for i,c in cdf if c <= r)
	return R


def weightedRandomIndex(pdf):
	'''
	returns the Index of probability array chosen by random
	pdf = [0.2, 0.4, 0.4]
	will return 0 or 1 or 2
	'''
	x = []
	for i in range(len(pdf)):
		x += [(i, pdf[i])]
	return weightedRandom(x)


if __name__ == '__main__':
	# j = [(0, 0.2), (1, 0.6), (2, 0.2)]
	# for i in range(100):
	# 	x = weightedRandomRange(j, [(-1,1) , (1,2) , (2,3)])
	# 	print(x)
	genStatement()
