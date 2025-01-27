#Write a Python program that prompts the user to enter a positive integer and then prints
#all the numbers from 1 to that number using a while loop.
my_num = 0
input_num = int(input("enter number "))
while my_num < input_num:
    my_num += 1
    print(my_num)