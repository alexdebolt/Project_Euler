# program to find value of the first triangle number to have over five hundred divisors
import math
import time
s= time.time()


def num_divisors(number):
    divisors = 0
    sqrt = int(math.sqrt(number))

    for i in range(1, sqrt + 1):
        if number % i == 0:
            divisors += 2
    
    if(sqrt * sqrt == number):
        divisors -= 1
    
    return divisors


number = 0
i = 1
while num_divisors(number) < 500:
    number += i
    i += 1

print(number)

# print(num_divisors(number))
print(time.time() - s)