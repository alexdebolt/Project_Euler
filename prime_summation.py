# algorithim to find sum of the primes below a certain number, in this case 2 million

def find_prime_summation():
    prime_number = [2]
    i = 100001
    while i > 2:
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            prime_number.append(i)

        i -= 2
        
    return sum(prime_number)

print(find_prime_summation())