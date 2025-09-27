import random
from random import randint
#By the way, this is CIF junior class 1 homework)
play = input('Would you like to play ? (y/n)')
between = int(input('Hello there! I am Clare the treasure box! The way you can open me is by geussing a number. If the number is correct, i will give you my treasure, but if not, the password will change!!!! You get to choose the limit of your number here!'))
my_number = randint(5, between)

while play == "y" or play == "yes":

    num= int(input('Now guess the number and cross your fingers!'))
    if num == my_number:
        print('wow! you guessed it right! you now get',my_number,"bucks (which was the treasure!)")
        play = "n"
    elif num <= my_number:
        print("Uh oh, your number was to small")
        play = input('Would you like to guess again? (y/n)')
    else:
        print('Uh oh, your number was to big. The number was',my_number,'. Good luck next time!')
        play = input('Would you like to guess again? (y/n)')

print('By the way, you played very well')