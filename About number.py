
num = int(input("Enter a number: "))

# 1. Check whether the original number is prime
if num > 1:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

# 2. Find the single digit sum
n = abs(num)

while n >= 10:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total

print("Single digit sum:", n)

# 3. If the single digit is not prime, print
# the ORIGINAL NUMBER'S factors

if n not in (2, 3, 5, 7):
    print("Single digit sum is not prime")

    print("Factors of the given number:")
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            print(i)

# 4. Check whether the original number is a palindrome
original = str(abs(num))

if original == original[::-1]:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")


