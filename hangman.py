import random

# Hangman visual stages
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

# Word list
word_list = ['banana', 'mango', 'apple', 'orange', 'kiwi', 'grape', 'papaya', 'pineapple', 'blueberry', 'strawberry', 'watermelon', 'peach', 'apricot' ,'book', 'pencil', 'school', 'window', 'ocean', 'planet', 'mountain', 'castle', 'rocket', 'forest', 'desert', 'bottle', 'guitar'

]
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]
lives = 6
gameover = False

print("🎮 Welcome to Hangman!")
print(display)

while not gameover:
    guess = input("Enter a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"❌ Incorrect! Lives remaining: {lives}")
        if lives == 0:
            gameover = True
            print("💀 You lose! The word was:", chosen_word)

    print(display)
    print(stages[6 - lives])

    if '_' not in display:
        gameover = True
        print("🎉 You win!")
