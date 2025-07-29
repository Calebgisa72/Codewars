# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wllef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence: str):
    reversedStr = []
    words = sentence.split(' ')
    for word in words:
        if len(word) >= 5:
            reversedStr.append(word[::-1])
        else:
            reversedStr.append(word)    
    return ' '.join(reversedStr)

print(spin_words("Hey fellow warriors" ))
