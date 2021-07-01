import random


word_dict = {
    "Brand": "Ford is what?",
    "Model": "Mustang is a faster car ",
    "year": 2020,
    "Gareeb Scientist": "Indian Science Youtuber",
    "Subway": "Metro Cities",
    "Abruptly": "In a sudden and unexpected way ",
    "Lucky": "Happening By Chance",
    "Luxary": "The enjoyment of expensive and beautiful things",
    "Transcript": "A written or printed copy of what somebody has said",
    "Mystify": "To make somebody confused because he/she cannot understand something",
    "Oxygen": "Present On Our Planet (Life Saver)",
    "Icebox": "A box full of ICE",
    "SpaceX": "First Private Company to Reland its orbital Rocket",
    "ISRO": "Indian1 Space Agency",
    "Skyroot": "Private Space Company of India ,name their Rocket as Vikram",
    "Divo": "Buggati Super Car",
    "Aventador": "Lamborghini Super Car",
    "Science": "Subject in which you learn about Natural Processes",
    "Computer": "Built to do Complex Task & Make person Life Easier",
    "Programming": "Process of writing Computer Programs"


}


while True:
    random_selection = random.choice(list(word_dict.keys()))

    # hints
    hint = str(word_dict[random_selection])
    char_count = len(random_selection)

    print(f'Hint:- {hint}')
    print(f"Length of word:- {char_count}")

    # turns
    turn = len(random_selection) + 3

    # empty string to store guessings of user
    guess = ''

    print(f"Total Turns:- {turn}")

    while turn > 0:
        failure = 0

        for char in random_selection.lower():
            if char in guess.lower():
                print(char, end=' ')
            else:
                print('_', end=' ')
                failure = failure+1

        if failure == 0:
            print('\nYou Won! Player')
            print('\nThe Word To be Guessed is:-' + str(random_selection))
            break

        while True:
            try:
                user_guess = input('\nEnter your guessing Letter:-')
                ug = user_guess.lower()
                break
            except:
                print('Invalid Input')

        guess = guess+ug
        #print(guess, random_selection.lower())

        '''
        if guess.lower() == random_selection.lower():
            print('You Won! Player')
            print('The Word To be Guessed is:-' + str(random_selection))
            break
            '''

        if ug not in random_selection.lower():
            turn = turn-1
            print('wrong guessing Try again , This time fingers Crossed!')
            print("Remaining Turns:- " + str(turn))
            if turn == 0:
                print("\nYou Loose, Pls Check you IQ Power")

        else:
            print('\nCorrect')
            turn = turn-1

    ask = int(input('Want to play again: Yes(1) or No(2)- '))
    if ask == 2:
        print('\n')
        break
