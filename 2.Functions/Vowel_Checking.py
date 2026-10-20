def is_vowel(ch):
    return ch.lower() in "aeiou"

ch = input("Enter a character: ")

if is_vowel(ch):
    print("True")
else:
    print("False")