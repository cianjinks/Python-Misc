def wordLen(string):
    return len(string.split()) # no separator passed to split -> assumes white space

print(wordLen("This is a test"))