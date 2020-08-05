# algo to find sum of even valued fib numbers below value of 4 million

def find_even_fib_sum():
    fib_numbers = [1,2]
    current_value = 0
    while current_value < 4000000:
        current_value = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(current_value)
    fib_numbers.pop()
    even_fib = [i for i in fib_numbers if i % 2 == 0]
    sum_fib = sum(even_fib)
    return sum_fib

print(find_even_fib_sum())