from itertools import permutations

def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65)

def change_letter(word, n):
    out = word[0:n] + next_alpha(word[n]).lower()
    return out + word[n+1:] if n < len(word) else out

def anagrams(word = 'database'):
    word = word.strip()
    r = []
    R = []
    n = 0
    for p in permutations(word):
        if len(r) == len(word):
            R.append(r)
            r = []
            n = 0
        w = ''.join(p)
        r.append((w, change_letter(w, n)))
        n += 1
    R.append(r)
    return { 'rows': R, 'word': word}