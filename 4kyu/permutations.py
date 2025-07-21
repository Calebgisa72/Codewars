# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!

# Examples:
# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

def permutations(s):
    res = []
    stack = []

    

    for chr in s:
        stack.append([chr])
    
    while stack:
        top = stack.pop()

        if len(top) == len(s):
            res.append(''.join(top))
        
        for chr in s:
            if chr not in top:
                newT = top[:]
                newT.append(chr)
                stack.append(newT)
    
    return res

print(permutations('aabb'))
