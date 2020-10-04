from phrasehunter.game import Game
from phrasehunter.phrases import phrases

if __name__ == "__main__":
    name = None
    while True:
        if name == None:
            new_game = Game(phrases, None)
            again = new_game.start()
            if again[0]:
                name = again[1]
                continue    
            else:
                print("\nThanks for playing {}".format(name))
                break
        else:
            new_game = Game(phrases, name)
            again = new_game.start()
            if again[0]:
                continue
            else:
                print("Thanks for playing {}".format(name))
                break
        
