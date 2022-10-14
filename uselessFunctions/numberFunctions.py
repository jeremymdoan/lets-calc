def numberIterator(num):
    num_array = str(num)
    final = ''
    for n in num_array:
        final += str( (int(n) + 1) % 10 )
    return { 'solution': final }