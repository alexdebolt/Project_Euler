# program to count number of letters required to write out numbers from 1 to 1000
# example: 342 (three hundred and forty-two)
# don't include spaces or hyphens

# allows conversion of number to words
import inflect
p = inflect.engine()


# helper function to translate numbers to words
def translate():
    numbers = [num for num in range(1, 1001)]
    nums_as_words = []
    for num in numbers:
        words = p.number_to_words(num)
        nums_as_words.append(words)

    return nums_as_words

array = translate()

# counting function
def counting(arr_words):
    count = 0
    for word in arr_words:
        for letter in word:
            if letter.isalpha():
                count += 1
    return count





print(counting(array))
