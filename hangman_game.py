import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = ["PYTHON", "ESPRESSO","DAILY","GOAL","MONEY","SMILE","BEAUTY","WITH","BRAIN","BIO","LAST"]
class Hangman():
    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(word_to_guess))

    def find_indexes(self, letter):

        return [i for i, char in enumerate(self.word_to_guess) if letter == char]
    def is_invalid_letter(self, input_):

        return input_.isdigit() or (input_.isalpha() and len(input_)>1)
        
    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print("".join(self.game_progress))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index]=letter

    def get_user_input(self):
        user_input = input("Please Enter Letter: ")
        return user_input
    
    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            #validating the user input
            if self.is_invalid_letter(user_input):
                print("\n¡input is not a letter!")
                continue
            if user_input in self.game_progress:
                print("you've already guessed this letter")
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)

                if self.game_progress.count('_')== 0:
                    print("the word is {0}".format(self.word_to_guess))
                    quit()

                else:
                    self.failed_attempts += 1
            print("\n¡OMG! You lost!")

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()