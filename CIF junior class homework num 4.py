from random import randint


# Function to set up questions
def setup_questions():
    lista = [
        ["True/False: The more your heart beats, the longer you live. ", ["True", "true"],
         "Not what you expect it to be"],
        ["What is the organ that filters waste from your blood? ", ["kidneys", "the kidneys", "Kidneys"],
         "There are two of them"],
        ["What is the largest organ? ", ["skin", "Skin"], "Where all your cuts happen"],
        ["What is the gas that your lungs exhale?", ["CO2", "carbon dioxide", "Carbon Dioxide"], "Starts with a 'C'"],
        ["How many miles per hour can your sneeze travel?", ['100mph', "100"], "More than 90"],
        ["How many stomach chambers does a cow have?", ["4", "four", "Four"], "More than 1"],
        ["What color is the spider's blood?", ["Blue", "blue"], "No hint"],
        ["What is the powerhouse of the cell?", ["mitochondria", "Mitochondria"], "No hint"]
    ]
    return lista


# Initialize HP
HP = 50


# Function to determine if a question is a bonus
def bonus():
    bonusques = [False, False, False, False, False, False, True, True]
    return bonusques


# Function to track which questions are finished
def done():
    listdone = [False, False, False, False, False, False, False, False]
    return listdone


# Setting up the game
questions_bank = setup_questions()
bonuses = bonus()
finished = done()

print(
    "Welcome toTBAG! You only have 50 Health. \n When you answer a question wrong, you lose some Health.\n You have 8 tries \n You get HP by answering questions.\n If you need a hint, type 'Hint'.\nYou can win the game when your HP gets to 150. You lose the game when you lose all your HP.\n Good luck!")

question_counter = 1

while HP < 150 and HP > 0 and question_counter <= 8:
    quesnum = randint(0, 7)
    while finished[quesnum]:
        quesnum = randint(0, 7)

    question = questions_bank[quesnum][0]
    answers = questions_bank[quesnum][1]
    hint = questions_bank[quesnum][2]

    resp = input("Question " + str(question_counter) + ": " + question)

    if resp.lower() == "hint":
        print("Hint: " + hint)
        resp = input("Try again: " + question)

    if resp in answers:
        is_bonus = bonuses[quesnum]
        if is_bonus:
            HP += 40
        else:
            HP += 20
        print("Incredible!! Your HP is now", HP)
    else:
        HP -= 30
        print("Incorrect! Your HP is now", HP)

    finished[quesnum] = True
    question_counter += 1

if HP >= 150:
    print('WOAH!!!!! You won!')
elif HP > 0:
    print('You ran out of tries!! Better luck next time!🍀')
else:
    print('You lost! Better luck next time!🍀')
