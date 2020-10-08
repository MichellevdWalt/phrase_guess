from phrasehunter.game import Game
from phrasehunter.phrases import phrase_objects

if __name__ == "__main__":
    name = None
    phrases = phrase_objects()
    new_game = Game(phrases)
    new_game.start()
