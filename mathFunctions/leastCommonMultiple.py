from mathFunctions.euclideanAlgorithm import euclideanAlgorithm

def leastCommonMultiple(a, b):
  return 0 if ((a == 0) or (b == 0)) else abs(a * b) / euclideanAlgorithm(a, b)

