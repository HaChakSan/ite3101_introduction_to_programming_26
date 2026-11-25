def reverse(text):
    word = ""
    for char in text:
        word = char + word
    return word
