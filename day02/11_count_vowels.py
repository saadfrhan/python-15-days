sentence = input("Enter a sentence: ")


def count_vowels(sentence: str):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count = count + 1
    return count


print(count_vowels(sentence))
