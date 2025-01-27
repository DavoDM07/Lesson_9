#Write a Python program that generates a random number between 1 and 100 and asks
#the user to guess the number. The program should give hints whether the guessed
#number is too high or too low until the correct number is guessed.
import random
i = 0
my_num = random.randint(1,100)
your_num = int(input("enter number "))
hushum1 = 'too low'
hushum2 = 'too high'
while i < 1:
    if your_num == my_num:
        print('right')
        i += 1
        break
    elif your_num < my_num:
        print(hushum1)
        your_num = int(input('try again '))
    else:
        print(hushum2)
        your_num = int(input('try again '))




