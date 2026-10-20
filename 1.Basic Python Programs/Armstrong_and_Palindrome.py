def armstrong(n):
    digits = str(n)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == n

def palindrome(n):
    return str(n) == str(n)[::-1]

n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

if palindrome(n):
    print("Palindrome number")
else:
    print("Not a Palindrome number")