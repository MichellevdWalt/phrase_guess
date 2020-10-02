# Create your Phrase class logic here.

class Phrase:

    current_guess = None

    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self):
        phrase = list(self.phrase)
        blanks = []
        print(phrase)
        for letter in phrase:
            if letter != " ":
                blanks.append("_")
            elif letter == " ":
                blanks.append(" ")
        self.current_guess = " ".join(blanks)
        print(self.current_guess)
        

        while True:
            complete = self.check_complete()
            print(complete)
            if complete:
                print("Congratulations!!!! You guessed the phrase")
                break
            else:
                guess = self.check_letter()
                print("Guess:" + guess)
                index = []
                start = 0
                for letter in phrase:
                    if letter == guess.lower():
                        if start != 0:
                            blanks[phrase.index(letter, start + 1)] = guess
                            start = phrase.index(letter, start + 1)
                        else:
                            blanks[phrase.index(letter)] = guess
                            start = phrase.index(letter)
                            
                self.current_guess = " ".join(blanks)
                print(self.current_guess)


    def check_letter(self):
        guess = None
        while True:
            correct = False
            guess = input("Please guess a letter:  ")
            phrase = self.phrase
            print(phrase)

            for letter in phrase:
                if letter == guess.lower():
                    correct = True

            if correct:
                print("You guessed right!")
                break     
            else:
                print("Nope, try again!")

        return guess


    def check_complete(self):
        complete = False
        if "_" in self.current_guess:
            return False
        else:
            return True


# new_game = Phrase("This Phrase")
# new_game.display()