import random
print('***************** WORD GUESSING GAME ***************** ')
name = input("What is your name? ")
print("Good Luck ! ",name)

repeat = True
while repeat == True :
    animals = ['cat','dog','fish','pig','birds','cow','chicken','goat','duck',
               'horse','rabbit','butterfly','frog','rat','snake']

    words = animals
    word = random.choice(words)

    print("Your word has",len(word), "letters.")

    if word in animals:
        print("Guess the Animal")
        print("Guess the Animal found in the community: ")

    guesses = ''
    life = 3

    while life > 0:
        failed = 0
        for i in word:
            if i in guesses:
                print(i)
            else:
                print("_")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break

        guess = input("guess a character:")
        guesses += guess

        if guess not in word:
            life -= 1
            print("Wrong")
            print("You have", + life, 'more life')

            if life == 0:
                exit("Thank you for playing")