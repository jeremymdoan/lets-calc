
def euclideanAlgorithmIterative(originalA, originalB):
  a = abs(originalA)
  b = abs(originalB)

  while (a and b and a != b):
    [a, b] = [a - b, b] if a > b else [a, b - a]
  return a or b