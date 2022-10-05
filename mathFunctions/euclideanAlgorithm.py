
def euclideanAlgorithm(originalA, originalB):
  a = abs(originalA)
  b = abs(originalB)
  return a if b == 0 else euclideanAlgorithm(b, a % b)
