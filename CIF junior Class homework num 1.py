import random
from random import randint
my_number = randint(5,25)
#By the way, this is CIF junior class 1 homework)
num = int(input('Hello there! I am Clare the treasure box! The way you can open me is by geussing a number between 5 and 25. If the number is correct, i will give you my treasure, but if not, the password will change!!!! Enter your number here!'))
if num == my_number:
    print('wow! you guessed it right! you now get',my_number,"bucks (which was the treasure!)")
elif num <= my_number:
    print("Uh oh, your number was to small. The number was",my_number,'Good luck next time!')
else:
    print('Uh oh, your number was to big. The number was',my_number,'. Good luck next time!')
