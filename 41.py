import string

def write_letters(filepath):
    with open(filepath, "w") as file:
        for i in string.ascii_lowercase:
            file.write(i + "\n")

write_letters("letters1.txt")