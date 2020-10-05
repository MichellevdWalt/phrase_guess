import random
from .phrase import Phrase
# from .phrases import phrases

class Game:
    def __init__(self, phrases, score, games, name=None, missed=0, active_phrase=None, guesses=[], current_guess=None):
        self.phrases = phrases
        self.score = score
        self.games = games
        self.name = name
        self.missed = missed
        self.active_phrase = active_phrase
        self.guesses = guesses
        self.current_guess = current_guess


    def start(self):
        self.welcome()
        self.get_random_phrase()
        start_phrase = Phrase(self.active_phrase)
        blanks = start_phrase.display(self.name)
        self.current_guess = "".join(blanks)

        while True:
            self.get_guess()
            guesses_len = len(self.guesses)
            current_guessed_letter = self.guesses[guesses_len - 1]
            correct = start_phrase.check_letter(self.name, current_guessed_letter, self.missed)
            if correct:
                index = []
                number = -1
                active_phrase = self.active_phrase
                for letter in active_phrase:
                    number += 1
                    if letter == current_guessed_letter.lower():
                        blanks[number] = current_guessed_letter
                self.current_guess = " ".join(blanks)
                complete = start_phrase.check_complete(self.current_guess)
                if complete:
                    again = self.game_over(complete)
                    break
                else:
                    print(self.current_guess + "\n")
            else:
                self.missed += 1
                if self.missed == 5:
                    again = self.game_over(False)
                    break

        if again[0]:
            return True, self.name, again[1]
        elif again[0] == False:
            return False, self.name, again[1]


    def get_random_phrase(self):
        number = random. randint(0,len(self.phrases)-1)
        self.active_phrase = self.phrases[number]


    def welcome(self):
        if self.name == None:
            print("Welcome to our phrase guessing game!\n")
            name = input("What is your name?  ")
            self.name = name
        else:
            print("\nWelcome to another round {} \n\nYour current score is {} out of {} games".format(self.name, self.score, self.games))


    def get_guess(self):
        repeated = False
        while True:
            guess = input("\n{}, please guess a letter from a-z  ".format(self.name))
            if guess.isalpha():
                for letter in self.guesses:
                    if letter.lower() == guess.lower():
                        repeated = True                        
                if repeated:
                    print("\nOh-Oh...You guessed that one already. \nBe careful, this might cost a life if incorrect!")
                    self.guesses.append(guess)
                else:
                    self.guesses.append(guess)
                break
            else:
                print("\nThat doesn't seem to be a valid letter from a-z. Please try again.\n\nDon't worry, no life was taken")
                continue
            


    def game_over(self, win):
        if win:
            print("Congratulations {}!!!! You guessed the phrase!!\n".format(self.name))
            print('The correct phrase was: "' + self.active_phrase + '"\n')
        else:
            print("Better luck next time!!\n")
        while True:
            again = input("Would you like to play again? y/n  ")
            if again.lower() == "y":
                return True, win
                break
            elif again.lower() == "n":
                return False, win
                break
            else:
                print("\nPlease type only a 'y' or 'n'\n")
                continue
