import math

def relu(x):
	if x > 1 :
		return 1
	elif x < 0 :
		return 0
	else:
		return x

def sigmoid(x):
	return 1 / (1 + math.exp(-1*(x-0.5)))
