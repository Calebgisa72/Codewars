# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!

# Examples:
# With input 'ab':
# Your function should return ['', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

def permutations(s):
    res = []
    stack = []

    from collections import Counter
    s_count = Counter(s)
    seen = set()

    for chr in s:
        stack.append([chr])
    
    while stack:
        top = stack.pop()

        if len(top) == len(s):
            perm = ''.join(top)
            if perm not in seen:
                res.append(perm)
                seen.add(perm)
        
        top_count = Counter(top)
        for chr in s:
            if s_count[chr] != top_count[chr]:
                newT = top[:]
                newT.append(chr)
                stack.append(newT)
    
    return res

print(permutations('aabc'))
