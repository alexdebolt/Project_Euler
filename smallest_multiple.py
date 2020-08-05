# program to find the smallest pos number that is evenly divisible by all numbers from 1 to N

def find_smallest_pos():
    found = False
    # start at 2520 because 1-10 are only divisible evenly by multiples of 2520
    # therefore you only need to search half of range starting at 11 instead
    num = 2520
    while found == False:
        num += 2520
        is_divis = True
        for i in range(11, 21):
            if num % i != 0:
                is_divis = False
                break
            # wont exit loop until anser is found
            # is_divis will always be false until answer
        if is_divis:
            found = True
    return num

    

print(find_smallest_pos())