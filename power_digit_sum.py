# program to find the sum of the digits of 2^nth power



def find_sum(n):
    # easy part is getting the answer to the exponent
    power = 2 ** n

    sum_digits = sum(int(digit) for digit in str(power))

    return sum_digits



print(find_sum(1000))