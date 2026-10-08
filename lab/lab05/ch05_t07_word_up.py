pyg = 'ay'

original = input('Enter a word:')
word = original.lower()

if len(original) > 0 and original.isalpha():
    first = word[0]
    print(original)
else:
    print('empty')
