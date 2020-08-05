# algo to find sum of all multiples of 3 or 5 below 1000

def find_sum():
    sum = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum
print(find_sum())