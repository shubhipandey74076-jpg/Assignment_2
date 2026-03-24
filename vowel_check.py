def check_vowel(check):
    if check in 'aeiouAEIOU':
        print("Letter Is Vowel :")
    else:
        print("Letter Is Not Vowel :")

letter = input("Enter a character: ")
check_vowel(letter)