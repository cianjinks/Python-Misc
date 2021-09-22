def count_words(filepath):
    with open(filepath, "r") as file:
        text = file.read()
        return len(text.split(" "))

print(count_words("words1.txt"))