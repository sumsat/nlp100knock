# encodin: utf-8
str1 = "パトカー"
str2 = "タクシー"
str3 = "".join([c1 + c2 for c1, c2 in zip(str1, str2)])
print(str3)
