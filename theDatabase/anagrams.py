from itertools import permutations

def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65)

def change_last_letter(word):
    return word[0:-1] + next_alpha(word[-1]).lower()

def anagrams(word = 'database'):
    r = []
    R = []
    for p in permutations(word):
        if len(r) > 8:
            R.append(r)
            r = []
        w = ''.join(p)
        r.append((w, change_last_letter(w)))
    R.append(r)
    return { 'rows': R, 'word': word}