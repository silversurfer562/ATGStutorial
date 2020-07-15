# def enterName():
#     name = ''
#     name = input('Enter a name:')
#     if name == 'Alice':
#          print('Hi, Alice')
#     elif name == 'Bob':
#         print('Hi, Bob')
#     else:
#         print('try again Bob')
#
# enterName()
# import pyinputplus as pyip
# def enterName():
#
#     name = pyip.inputStr (prompt='Enter your name: ')
#     if name == 'Alice':
#          print('Hi, Alice')
#     elif name == 'Bob':
#         print('Hi, Bob')
#     else:
#     print('try again Bob')
#
# enterName()


# def enterPassword():
#     name = 'swordfish'
#     name = pyip.inputStr (prompt='Enter your password: ')
#     if name == 'swordfish':
#         print('Access granted')
#     else:
#         print('Access denied')
#
# enterPassword()


# import pyinputplus as pyip
# name = 'Bob'
# age = 0
# print('Enter your age: ')
# age = pyip.inputInt()
# if age < 12:
#     print('You are not Alice, kiddo')
# elif age > 2000:
#     print('Unlike you, Alice is not a vampire.')
# elif age > 100:
#     print('You are not Alice, granny.')
# else:
#     print('nice try' + name)

# spam = 0
# while spam < 5:
#     print('Hello World')
#     spam = spam + 1

# import pyinputplus as pyip
#
# def inputMyName():
#     name = ''
#     while name != 'patrick':
#         print('Please type your name: ')
#         name = input()
#         str.lower(name)
#         if name == 'patrick':
#             print('Good job Patrick')
#             break
#         elif name == 'Patrick':
#             print('try it lower case')
#     print ('thank you')
#
# inputMyName()

# example of a while loop using continue and break and validation for numbers greater than 5.
# import pyinputplus as pyip
# spam = 0
# spam = pyip.inputInt(prompt='enter a number between 1 and 5: ')
# while spam > 0:
#     if spam != 3:
#         print ('Try again. That number is not it.')
#         spam = pyip.inputNum(prompt='enter a number between 1 and 5: ', lessThan=6)
#         continue
#     elif spam == 3:
#         print("that's right. Spam is " + str(spam))
#         break




