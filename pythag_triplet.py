# program to find pythag triplet where a + b + c = 1000

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


