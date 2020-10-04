import random
import phrase
import phrases

class Game:
    
    def __init__(self, phrases, name=None, missed=0, active_phrase=None, guesses=[], current_guess=None):
        self.missed = missed
        self.name = name
        self.phrases = phrases
        self.active_phrase = active_phrase
        self.guesses = guesses
        self.current_guess = current_guess

    def start(self):
        self.welcome()
        self.get_random_phrase()
        start_phrase = phrase.Phrase(self.active_phrase)
        blanks = start_phrase.display(self.name)
        self.current_guess = "".join(blanks)

        while True:
            self.get_guess()
            current_guessed_letter = self.guesses[-1]
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

        if again:
            return True, self.name
        elif again == False:
            return False, self.name


    def get_random_phrase(self):
        number = random. randint(0,len(self.phrases)-1)
        self.active_phrase = self.phrases[number]


    def welcome(self):
        print(self.name)
        if self.name == None:
            print("Welcome to our phrase guessing game!\n")
            name = input("What is your name?  ")
            self.name = name
        else:
            print("Welcome to another round {}".format(self.name))


    def get_guess(self):
        guess = input("\n{}, please guess a letter from a-z  ".format(self.name))
        self.guesses.append(guess)


    def game_over(self, win):
        if win:
            print("Congratulations {}!!!! You guessed the phrase!!\n".format(self.name))
            print('The correct phrase was: "' + self.active_phrase + '"\n')
            again = input("Would you like to play again? y/n ")
        else:
            print("Better luck next time!!\n")
            again = input("Would you like to play again? y/n  ")
        if again.lower() == "y":
            return True
        elif again.lower() == "n":
            return False
