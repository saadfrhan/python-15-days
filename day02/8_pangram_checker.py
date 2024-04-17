sentence = input("Enter a sentence: ")


def is_pangram(sentence: str):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_letters = set(sentence.lower())

    return alphabet.issubset(sentence_letters)


if is_pangram(sentence) == True:
    print("Pangram")
else:
    print("Not a pangram")
