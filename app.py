from phrasehunter.game import Game
from phrasehunter.phrases import phrases

if __name__ == "__main__":
    name = None
    score = 0
    games = 0
    while True:
        if name == None:
            new_game = Game(phrases, score, games, None)
            again = new_game.start()
            if again[0]:
                name = again[1]
                games += 1
                if again[2]:
                    score +=1
                continue    
            else:
                name = again[1]
                print("\nThanks for playing {}".format(name))
                if again[2]:
                    score += 1
                games += 1
                print("\nYour final score was {} out of {}".format(score, games))
                break
        else:
            new_game = Game(phrases, score, games, name)
            again = new_game.start()
            if again[0]:
                if again[2]:
                    score +=1
                games += 1
                continue
            else:
                print("\nThanks for playing {}".format(name))
                if again[2]:
                    score += 1
                games += 1
                print("\nYour final score was {} out of {}".format(score, games))
                break
        
