d = {"a": 1, "b": 2, "c": 3}

i = 0
for k in d:
    i += d[k]

print(i)

# also
j = sum(d.values())
print(j)