# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import Player, Game

if __name__ == "__main__":
    player1_name = input("Enter name for Player 1: ")
    player1_symbol = input("Enter symbol for Player 1 (X or O): ")
    player1 = Player(player1_name, player1_symbol)

    if player1_symbol.upper() == 'X':
        player2_symbol = 'O'
    elif player1_symbol.upper() == 'O':
        player2_symbol = 'X'
    else:
        print("Invalid symbol for Player 1. Exiting.")
        exit()

    player2 = Player("Bot", player2_symbol)

    game_mode = input("Enter game mode (1 for single player, 2 for two players): ")

    if game_mode == '1':
        player2 = Player("Bot", player2_symbol)
    elif game_mode != '2':
        print("Invalid game mode. Exiting.")
        exit()

    game = Game(player1, player2)
    game.start_game()
