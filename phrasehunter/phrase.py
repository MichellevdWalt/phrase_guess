# Create your Phrase class logic here.

class Phrase:
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
        print("\n" + " ".join(blanks))
        return blanks


    def check_letter(self, name, guess, lives):
        correct = False
        phrase = self.phrase

        for letter in phrase:
            if letter == guess.lower():
                correct = True

        if correct:
            print("\nYou guessed right!\n")     
        else:
            print("\nNope, you have {} out of 5 lives remaining\n".format(5-(lives+1)))

        return correct


    def check_complete(self, current_guess):       
        if "_" in current_guess:
            return False
        else:
            return True
