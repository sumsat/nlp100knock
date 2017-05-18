# coding: utf-8
def cipher(string):
    replaced = ''.join([chr(219 - ord(c)) if c.islower() else c for c in string])
    return replaced

string = "This is a message in English."
print(cipher(string))
