# coding: utf-8
from k05 import ngram_char

str1 = "paraparaparadise"
str2 = "paragraph"
set_x = set(ngram_char(str1, 2))
set_y = set(ngram_char(str2, 2))

print("和集合: {}".format(set_x | set_y))
print("積集合: {}".format(set_x & set_y))
print("差集合: {}".format(set_x - set_y))

if 'se' in set_x:
    print("\'se\'はXに含まれる")
else:
    print("\'se\'はXに含まれない")
if 'se' in set_y:
    print("\'se\'はYに含まれる")
else:
    print("\'se\'はYに含まれない")
