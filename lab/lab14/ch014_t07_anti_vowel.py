def anti_vowel(text):
    word = ""
    for i in text:
        if i not in "aeiouAEIOU":
            word = word + i
    return word