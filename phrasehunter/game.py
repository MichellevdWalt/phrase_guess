import random

import phrase
import phrases
print(phrases.phrases)

class Game:
    # phrases = phrases.phrases
    name = None
    def __init__(self, phrases, missed=0, active_phrase = None, guesses=[], current_guess=None):
        self.missed = missed
        self.phrases = phrases
        self.active_phrase = active_phrase
        self.guesses = guesses
        self.current_guess = current_guess

    def start(self):
        self.welcome()
        self.get_random_phrase()
        start_phrase = phrase.Phrase(self.active_phrase)
        start_phrase.display(self.name)
        blanks = start_phrase.display(self.name)
        self.current_guess = "".join(blanks)
        while True:
            self.get_guess()
            current_guessed_letter = self.guesses[-1]
            correct = start_phrase.check_letter(self.name, current_guessed_letter)
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
                print(complete)
                if complete:
                    print("Congratulations {}!!!! You guessed the phrase!!\n".format(self.name))
                    print('"' + self.active_phrase + '"')
                    break
                else:
                    print(self.current_guess)
            

        #start(): Calls the welcome method, creates the game loop, calls the get_guess method,
        #  adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect,
        #  calls the game_over method.

    def get_random_phrase(self):
        number = random. randint(0,len(self.phrases)-1)
        self.active_phrase = self.phrases[number]

    def welcome(self):
        print("Welcome to our phrase guessing game!")
        name = input("What is your name?  ")
        self.name = name

    def get_guess(self):
        guess = input("{}, please guess a letter from a-z  ".format(self.name))
        self.guesses.append(guess)

    def game_over(self):
        # game_over(): this method displays a friendly win or loss message and ends the game.
        pass


new_game = Game(phrases.phrases)
new_game.start()