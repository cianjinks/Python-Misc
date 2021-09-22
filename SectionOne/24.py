d = {
    "a": list(range(1, 11)),
    "b": list(range(11, 21)),
    "c": list(range(21, 31))
}

for key in d:
    print(key, "has value", d[key])

# also
for k, v in d.items():
    print(k, "has value", v)