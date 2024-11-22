import random

rock='''
      _-''-_
_____'   ''-__)
        ( _____)
         (______)
____    (______)
    '---(____)
                 
'''

paper='''
     ____
____'    '_____)
            ________)
             _________)
___        _________)
   '-----_________)            


'''

scissors='''
    _______
___'    _____)____
            ______)
        ___________)
____    (____)
    '___(___)

'''

times = int(input("how many time you want to play"))

for i in range(0,times):

    list = [rock, paper, scissors]

    comp_choice = random.choice(list)

    user_choice = input("r for rock,p for papers, s for scissors")




    if user_choice == "r":

        print("your choice",rock)
        if comp_choice == paper:
            print(paper,"you lose")

        elif comp_choice==scissors:
            print(scissors,"you win")
        else:
            print(rock,'tie')

    elif user_choice=="p":
        print(paper,"your choice")
        if comp_choice == scissors:
            print(scissors, "you lose")

        elif comp_choice == rock:
            print(rock, "you win")
        else:
            print(paper, 'tie')
    elif user_choice == "s":
        print(scissors, "user choice")
        if comp_choice == rock:
            print(rock, "you lose")

        elif comp_choice == paper:
            print(paper, "you win")
        else:
            print(scissors, 'tie')

    else:
        print("wrong choice ")



