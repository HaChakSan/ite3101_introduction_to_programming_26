# Setup Pig Latin suffix
pyg = 'ay'

# Get word input from user
original = input('Enter a word: ')

# Check that the input is valid (not empty and contains only letters)
if len(original) > 0 and original.isalpha():
    # Convert word to lowercase for uniform processing
    word = original.lower()
    
    # Store the first letter
    first = word[0]
    
    # Append the first letter and 'ay' suffix to the word
    new_word = word + first + pyg
    
    # Remove the initial first letter by slicing from index 1 to the end
    new_word = new_word[1:len(new_word)]
    
    # Print the translated Pig Latin word
    print(new_word)
else:
    print('empty')