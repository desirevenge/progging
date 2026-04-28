import imp
from itertools import *
k = 0
for x in product('ЕЛНОСЦ', repeat=5):
    s = ''.join(x)
    k+=1
    if 'Л' not in s and s.count('Е')<=1:
        print(k,s)
        break
