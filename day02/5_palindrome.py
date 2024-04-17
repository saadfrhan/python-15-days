word = input("Enter a word: ")

reveresed = word[::1]

if reveresed == word:
    print("palindrome")
else:
    print("not a palindrome")
