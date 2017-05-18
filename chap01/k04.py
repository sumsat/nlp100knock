# coding: utf-8
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = text.split(' ')
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {w[0] if i + 1 in single else w[0:2]: i + 1 for i, w in enumerate(words)}
print(dic)
