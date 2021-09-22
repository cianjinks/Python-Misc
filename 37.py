def count_words(filepath):
    text = ""
    
    with open(filepath, "r") as file:
        text = file.read()

    text = text.replace(",", " ")
    return len(text.split(" "))

print(count_words("words2.txt"))