# method to find the difference between the sum of the squares and the square 
# of the sum of the first 100 numbers

def find_difference():
    sum_sq = 0
    sum_before_sq = 0
    for i in range(1, 101):
        sum_sq += (i ** 2)
        sum_before_sq += i

    return (sum_before_sq ** 2) - sum_sq


print(find_difference())