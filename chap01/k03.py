# coding: utf-8
import re
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split(r'[^a-zA-Z]', text)
num = [len(word) for word in [word for word in words if word]]
print(num)
