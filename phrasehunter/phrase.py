# Create your Phrase class logic here.

class Phrase:

    current_guess = None

    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self, name):
        phrase = list(self.phrase)
        blanks = []
        for letter in phrase:
            if letter != " ":
                blanks.append("_")
            elif letter == " ":
                blanks.append(" ")
        print(" ".join(blanks))
        return blanks
        

        # while True:
        #     complete = self.check_complete()
        #     print(complete)
        #     if complete:
        #         print("Congratulations {}!!!! You guessed the phrase".format(name))
        #         break
        #     else:
        #         guess = self.check_letter(name)
        #         print("Guess:" + guess)
        #         index = []
        #         start = 0
        #         for letter in phrase:
        #             if letter == guess.lower():
        #                 if start != 0:
        #                     blanks[phrase.index(letter, start + 1)] = guess
        #                     start = phrase.index(letter, start + 1)
        #                 else:
        #                     blanks[phrase.index(letter)] = guess
        #                     start = phrase.index(letter)
                            
        #         self.current_guess = " ".join(blanks)


    def check_letter(self, name, guess):
        correct = False
        phrase = self.phrase

        for letter in phrase:
            if letter == guess.lower():
                correct = True

        if correct:
            print("You guessed right!")     
        else:
            print("Nope, try again!")

        return correct


    def check_complete(self, current_guess):
        complete = False
        if "_" in current_guess:
            return False
        else:
            return True


# new_game = Phrase("This Phrase")
# new_game.display()