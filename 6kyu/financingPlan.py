# I need to save some money to buy a gift. I think I can do something like that:

# First week (W0) I save nothing on Sunday, 1 on Monday, 2 on Tuesday... 6 on Saturday, second week (W1) 2 on Monday... 7 on Saturday and so on according to the table below where the days are numbered from 0 to 6.

# Can you tell me how much I will have for my gift on Saturday evening after I have saved 12? (Your function finance(6) should return 168 which is the sum of the savings in the table).

# Imagine now that we live on planet XY140Z-n where the days of the week are numbered from 0 to n (integer n > 0) and where I save from week number 0 to week number n included (in the table below n = 6).

# How much money would I have at the end of my financing plan on planet XY140-n?

# --	Su	Mo	Tu	We	Th	Fr	Sa
# W6							12
# W5						10	11
# W4					8	9	10
# W3				6	7	8	9
# W2			4	5	6	7	8
# W1		2	3	4	5	6	7
# W0	0	1	2	3	4	5	6

def finance(n):
    # total = 0
    # for i in range(n+1):
    #     for j in range(i,n+1):
    #         total += j+i
    
    # return total

    return (n+2) * (n+1) * n / 2

print(finance(5000))

# finance(5) --> 105
# finance(6) --> 168
# finance(7) --> 252
# finance(5000) --> 62537505000

