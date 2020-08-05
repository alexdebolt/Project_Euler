# program to find the 10,001st prime number
import time
s = time.time()

def find_prime_number():
    prime_nums = [2]
    i = 3
    while len(prime_nums) < 10001:
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            prime_nums.append(i)

        i += 2

    return prime_nums




print(find_prime_number())
print(time.time() - s)