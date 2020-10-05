Treehouse Python Techdegree Project - Unit 3

This is a classic guess-the-phrase in-command-line game. 

The player is welcomed to the game

-Extra- The player is prompted for his or her name which is then stored for personalized experience throughout the rest of play. 

A random phrase from a selection of phrases is selected and displayed as _ _ _ underscores.

The player then proceeds to guess a letter at a time. 
    -Exceeds- If the player enters either a numeral or more than one char an error message shows and prompts the player to try again
    -Extra- If the player guesses a letter they have already guessed it displays a warning to the player indicating that they have guessed that letter before. If incorrect, this will still cost a life
    -If the player guesses a char correctly a message is displayed and the player prompted for another letter if the phrase is not complete.
    -If the player guesses incorrectly a message is displayed as well as indication of lives remaining. 

-Exceeds- After each game the player is prompted whether they want to play another game
    - Only Y/y or N/n is accepted otherwise it displays an error
    - If y, a new instance is created and -extra- the players current score is displayed
        -extra- The player is welcomed back by name and not prompted for their name again
    - If n, the player is thanked for playing -extra- and the players current score is displayed.
