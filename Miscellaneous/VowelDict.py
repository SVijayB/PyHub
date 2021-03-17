# Create a dictionary with keys as string (taken from input) and value as the number of vowels in that string


def Count_Vowel(string):
    vowels = "aeiou"
    string = string.casefold()
    count = 0
    for character in string:
        if character in vowels:
            count = count + 1
    return count


if __name__ == "__main__":
    result = dict()
    n = int(input("Enter number of words you want to enter : "))
    for i in range(n):
        word = input("Enter the word : ")
        count = Count_Vowel(word)
        result.update({word: count})

    print(result)
