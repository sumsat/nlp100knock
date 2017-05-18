# coding: utf-8
import numpy as np

def typoglycemia(text):
    words = text.split(' ')
    replaced = [''.join(np.hstack((w[0], np.random.permutation(list(w[1:-1])), w[-1]))) if len(w) > 4 else w for w in words]
    return ' '.join(replaced)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(text))
