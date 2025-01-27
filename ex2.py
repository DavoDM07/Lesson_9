#Write a Python program that calculates the sum of all even numbers between 1 and 100
#using a while loop.

result = 0
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        result += i
print(result)

