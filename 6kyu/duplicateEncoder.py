# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"

def duplicate_encode(word):
    word = word.lower()
    seen = {}
    for chr in word:
        seen[chr] = seen.get(chr,0) + 1
    
    return "".join('(' if seen[ch] == 1 else ')' for ch in word)

print(duplicate_encode("Success"))