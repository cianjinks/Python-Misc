a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

b = ["1", 1, "1", 2]
c = []
for i in b:
    if i not in c:
        c.append(i)
print(c)
