# MaxProfit

# Imagine you're buying and selling stocks throughout the year. Your job is to find the biggest profit you could make by buying low, and selling high only once

# Here’s what you’re given: A list of stock prices for each day 👉 [7, 1, 5, 3, 6, 4]

# Here’s what you need to find: The difference between the cheapest price you could have bought the stock and the most expensive price you could have sold it later on.

def maxProfit(stocks):
    maxNum = stocks[0]
    minNum = stocks[0]
    for num in stocks:
        if num < minNum:
            maxNum = num
            minNum = num
        elif num > maxNum:
            maxNum = num  
            
    return maxNum - minNum

print(maxProfit([7, 1, 5, 3, 6, 4]))
            
            
