# Rock, Paper, Scissors, Lizard, Spock

## Description

The game "rock-paper-scissors-lizard-spock" is an extension of the commonly known game "rock-paper-scissors". Rock-paper-scissors-lizard-spock adds two additional moves to the basic game. The rules are summarized both in this educational video: http://youtu.be/iapcKVn7DdY, and the image below. The arrows indicate which move beats which. For example, the arrow from paper to Spock indicates that paper disproves Spock (if one player plays paper, and the other plays Spock, the one that played paper wins).

![image](https://user-images.githubusercontent.com/86201781/128752719-4a56792a-fae0-44ad-9ace-6808a62bd7f3.png)

## Problem description

There are 25 possible pairs of moves, so sometimes it’s hard to remember them. The program will act as a referee. The program will ask for the moves made by the two players via console input and report which player won.

To solve this problem, a function will be accepting two moves made by the players as arguments, and returning the outcome. Separately, a main program will perform the console input to request player 1’s move, and player 2’s move, and then call the function to determine the outcome.

Note: The computer is not one of the players, the computer only determines who won given the moves that the two human players made.

Sample input and output (input typed by the user is shown in green text) for two different runs, the first showing a winner, the second showing a tie

![image](https://user-images.githubusercontent.com/86201781/128753212-2c92d56c-256f-4e53-b503-c7dd403b134c.png)
