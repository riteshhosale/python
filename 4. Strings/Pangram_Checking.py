import string

def pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())

s = input("Enter a sentence: ")

if pangram(s):
    print("Pangram")
else:
    print("Not a Pangram")