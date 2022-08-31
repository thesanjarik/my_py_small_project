import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play_word(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давайте поиграем в Палача!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Пожалуйста, угадайте букву или слово: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадали букву", guess)
            elif guess not in word:
                print(guess, "его нет в этом мире.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("хорошая работа,", guess, "есть в мире!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже угадали это слово", guess)
            elif guess != word:
                print(guess, "это не то слово.")
                tries -= 1
                guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
            print("Неверное предположение.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Поздравляю, вы угадали слово! Ты победил!")
    else:
        print("Извини, у тебя закончились все попытки. Это слово было" + word + ".Может быть, в следующий раз!")


def display_hangman(tries):
    stages = [ """
                 --------
                 |      |
                 |      0
                 |      \\|/
                 |      |
                 |      / \\
                 -
    """,
               """
                 --------               
                 |      |
                 |      0
                 |      \\|/
                 |      |
                 |      / 
                 -
               """,
               """
                 --------              
                 |      |
                 |      0
                 |      \\|/
                 |       |
                 |      / \\
                 -
               """,
               """
                 --------                             
                 |      |
                 |      0
                 |      \\|/
                 |      |
                 |      / 
                 -
               """,
               """
                 --------                             
                 |      |
                 |      0
                 |      \\|/
                 |       |
                 |      
                 -
               """,
               """
                 --------                             
                 |      |
                 |      0
                 |      \\|
                 |       |
                 |      
                 -
               """,
               """
                 --------                             
                 |      |
                 |      0
                 |      |
                 |      |
                 |      
                 -
               """,
               """
                 --------                             
                 |      |
                 |      0
                 |      
                 |      
                 |      
                 -
               """,
               """
                 --------                             
                 |      |
                 |      
                 |      
                 |      
                 |      
                 -
               """

    ]

    return stages[tries]

def main():
    word = get_word()
    play_word(word)


if __name__ == "__main__":
    main()
