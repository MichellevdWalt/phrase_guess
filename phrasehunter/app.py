# Import your Game class
import game
import phrases
# Create your Dunder Main statement.
if __name__ == "__main__":
    name = None
    while True:
        if name == None:
            new_game = game.Game(phrases.phrases, None)
            again = new_game.start()
            if again[0]:
                name = again[1]
                continue    
            else:
                print("\nThanks for playing {}".format(name))
                break
        else:
            new_game = game.Game(phrases.phrases, name)
            again = new_game.start()
            if again[0]:
                continue
            else:
                print("Thanks for playing {}".format(name))
                break
        


# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
