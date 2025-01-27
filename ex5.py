#Write a Python program that calculates the Fibonacci sequence up to a given number n
#using a while loop. The Fibonacci sequence is a series of numbers where each number
#is the sum of the two preceding ones

num_i_gave = int(input('enter number '))
x, y = 0, 1
fibonacci_list = []
while x <= num_i_gave:
    fibonacci_list.append(x)
    x, y = y, x + y
print(fibonacci_list)



