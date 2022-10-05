from math import sqrt

def quadractricFormula(a, b, c):
	isReal = True
	d = (b ^ 2) - (4 * a * c)
	if (d < 0):
		isReal = False
		sol1 = '( -{0} - sqrt({1}) ) / {2}'.format(b, d, 2*a)
		sol2 = '( -{0} + sqrt({1}) ) / {2}'.format(b, d, 2*a)
	else:
		sol1 = (-b - sqrt(d)) / (2 * a)
		sol2 = (-b + sqrt(d)) / (2 * a)
	solutions = [sol1, sol2]
	return {
		'isReal': isReal,
		'solutions': solutions
	}
