def main():
    """
    A program to play The Ancient Game of Nimm
    Game starts with a pile of 20 stones between two players 
    The two players take turns to play
    On a given turn, a player may take either 1 or 2 stone from the center pile 
    The two players continue until the center pile has run out of stones 
    The last player to take a stone loses
    """
    stones = 20
    player = 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        msg = f"Player {player} would you like to remove 1 or 2 stones? "
        stone_removed = int(input(msg))
        if stone_removed != 1 and stone_removed != 2: 
            stone_removed = int(input("Please enter 1 or 2: "))
        stones = stones - stone_removed
        print("")

        # if stones left = 0, game ends
        if stones == 0:
            if player == 1: # the last player to remove stones 
                winner = 2 # the winner is the other person
            else: 
                winner = 1
            print(f"Player {winner} wins!")
            break

        # Switch player 
        player = 2 if player == 1 else 1
        

if __name__ == '__main__':
    main()