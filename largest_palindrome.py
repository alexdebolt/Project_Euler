# program to find largest palindrome made from the product of two 3-digit numbers



# method will use a string conversion to compare digits
def find_palindrome_numstring(num):
    stringed_num = str(num)
    if len(stringed_num) < 2:
        return True
    if stringed_num[0] != stringed_num[-1]:
        return False
    return find_palindrome_numstring(stringed_num[1:-1])


# method to multiply three digit numbers together
def find_product():
    palindrome = []
    for i in range(999, 100, -1):
        for n in range(i, 100, -1):
            number = i * n
            if find_palindrome_numstring(number):
                palindrome.append(number)
    return max(palindrome)
        
print(find_product())