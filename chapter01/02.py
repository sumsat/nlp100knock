# encodin: utf-8
str1 = "パトカー"
str2 = "タクシー"
str3 = ""
for c1, c2 in zip(str1, str2):
    str3 += c1 + c2
print(str3)
