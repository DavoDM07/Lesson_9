#Write a Python program that asks the user to enter a password. Keep asking for the
#password until the correct password "secret" is entered. Provide appropriate feedback
#to the user

key = 0
password = 'secret'
your_attempt = str(input('enter password '))
while key < 1:
    if your_attempt == password:
        key += 1
        print('you have successfully logged into your account')
        break
    else:
        your_attempt = str(input('wrong password try again '))


