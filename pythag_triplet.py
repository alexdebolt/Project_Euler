# program to find pythag triplet where a + b + c = 1000
import time
start_time = time.time()


def find_pytha_triplet():
    for m in range(2, 500):
        for n in range(1, m):
            a = (m**2) - (n**2)
            b = 2 * m * n
            c = (m**2) + (n**2)
            sum = a + b + c
            if sum == 1000:
                print(a, b, c)
                print(sum)
                return a * b * c
            
print(find_pytha_triplet())


# the above formula is very straight forward, trying a simpler version with an augmented equation
def simple_pyth():
    for m in range(2, 500):
        for n in range(1, m):
            variable = m * (m + n)
            if variable == 500:
                a = (m**2) - (n**2)
                b = 2 * m * n
                c = (m**2) + (n**2)
                return a * b * c

print(simple_pyth())
# second method cut time by more than half

print("--- %s seconds ---" % (time.time() - start_time))