from phrasehunter.game import Game
from phrasehunter.phrases import phrase_objects

if __name__ == "__main__":
    name = None
    phrases = phrase_objects()

    while True:
        if name == None:
            new_game = Game(phrases, name = None)
            again = new_game.start()
            if again[0]:
                name = again[1]
                continue    
            else:
                name = again[1]
                print("\nThanks for playing {}".format(again[1]))
                print("\nYour final score was {} out of {}".format(again[2], again[3]))
                break
        else:
            new_game = Game(phrases, score = again[2], games = again[3], name=name, missed=0, active_phrase=None, guesses=[], current_guess=None)
            again = new_game.start()
            if again[0]:
                continue
            else:
                print("\nThanks for playing {}".format(name))
                print("\nYour final score was {} out of {}".format(again[2], again[3]))
                break
        
