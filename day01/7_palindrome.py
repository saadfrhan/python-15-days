word = input("Enter a word: ")

reversed = word[::-1]

if reversed == word:
    print("It's a palindrome!")
else:
    print("Not a palindrome")
