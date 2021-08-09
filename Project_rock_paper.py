player1 = input("Player 1 chooses their move: ")
player2 = input("Player 1 chooses their move: ")
def rock_paper_scissors_lizard_spock():
    """
    The function is calculating(judging) the outcome of the game of rock, paper, scissors, lizard, spock
    w1: a string that represents that the player one won the round
    w2: a string that represents that the player two won the round
    tie: a string that represents the tie in the round
    x: string that represents the first input of the user or the input of the first player
    y: string that represents the second input of the user or the input of the second player
    returns: w1, w1 and tie: strings that represents that the player 1 wins the game, player 2 wins the game and it's a
    tie between the players respectively
    """
    x = player1
    y = player2
    w1 = "Player 1 won!"
    w2 = "Player 2 won!"
    tie = "It's a tie!"

    if x == "rock" and (y == "scissors" or y == "lizard"):
        return w1
    if x == "rock" and (y == "paper" or y == "spock"):
        return w2
    if x == "rock" and y == "rock":
        return tie

    if x == "paper" and (y == "rock" or y == "spock"):
        return w1
    if x == "paper" and (y == "scissors" or y == "lizard"):
        return w2
    if x == "paper" and y == "paper":
        return tie

    if x == "scissors" and (y == "paper" or y == "lizard"):
        return w1
    if x == "scissors" and (y == "rock" or y == "spock"):
        return w2
    if x == "scissors" and y == "scissors":
        return tie

    if x == "spock" and (y == "scissors" or y == "rock"):
        return w1
    if x == "spock" and (y == "paper" or y == "lizard"):
        return w2
    if x == "spock" and y == "spock":
        return tie

    if x == "lizard" and (y == "paper" or y == "spock"):
        return w1
    if x == "lizard" and (y == "scissors" or y == "rock"):
        return w2
    if x == "lizard" and y == "lizard":
        return tie

print(rock_paper_scissors_lizard_spock())
