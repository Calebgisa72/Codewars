# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.
# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

# If it is the case we will return k, if not return -1.
# Note: n and p will always be strictly positive integers.

# Examples:
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

def dig_pow(n, p):
    sumOfPowers = sum(int(x)**(p+i) for i, x in enumerate(str(n)))
    k = sumOfPowers/n
    return int(k) if k.is_integer() else -1

print(dig_pow(89, 1))
print(dig_pow(46288, 3))