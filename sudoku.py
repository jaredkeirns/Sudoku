# Jared Keirns
# CS325 - Portfolio Project Code
# A sudoku game program with one board. The player can place valid inputs (integers 1-9), into valid locations
# within the board that were not occupied by an 'original' numbers (numbers that were already placed on the original
# board). When all the board locations are occupied, the program will run a validation function to see if the board is
# correct. The board is correct if each row contains numbers 1-9 with none repeating, each column contains numbers 1-9
# with none repeating, and each sub-square contains numbers 1-9 with none repeating. To easily check the algorithm
# the player can enter 'ANSWER' for the program's first request ("Please enter row number: "), and the program will
# send the 'answer' board to the validation function to check it.


user_grid = [                               # The users starting puzzle board.
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 3, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

original_grid = [                           # A copy of the original board.
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 3, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

answer_grid = [                             # The correct, complete board.
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


def game_end(user_grid):
    """
    A function that determines if the completed grid is correct by checking if each row, column and sub-square
    contains 1-9
    """
    for rows in user_grid:                  # Validates each row contains 1-9.
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for elements in rows:
            if elements in test_list:
                test_list.remove(elements)
            else:                           # There was repetition within the row.
                print("Puzzle was not solved correctly.")
                return
    i = 0
    j = 0
    while j <= 8:                           # Validates each column contains 1-9
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for rows in user_grid:
            if rows[i] in test_list:
                temp = rows[i]
                test_list.remove(temp)
            else:                           # There was repetition within the column.
                print("Puzzle was not solved correctly.")
                return
        i += 1
        j += 1

    j = 0
    k = 0                                   # Validates each sub-square contains 1-9.
    l = 0
    while l < 1:                            # Will need to do this for all 9 sub squares.
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 2:
            while j <= 2:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:                       # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 0
            k += 1

        j = 3
        k = 0
        l += 1

    while l < 2:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 2:
            while j <= 5:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 3
            k += 1

        j = 6
        k = 0
        l += 1

    while l < 3:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 2:
            while j <= 8:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 6
            k += 1

        j = 0
        k = 3
        l += 1

    while l < 4:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 5:
            while j <= 2:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 0
            k += 1

        j = 3
        k = 3
        l += 1

    while l < 5:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 5:
            while j <= 5:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 3
            k += 1

        j = 6
        k = 3
        l += 1

    while l < 6:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 5:
            while j <= 8:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 6
            k += 1

        j = 0
        k = 6
        l += 1

    while l < 7:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 8:
            while j <= 2:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 0
            k += 1

        j = 3
        k = 6
        l += 1

    while l < 8:
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while k <= 8:
            while j <= 5:
                if user_grid[k][j] in test_list:
                    temp = user_grid[k][j]
                    test_list.remove(temp)
                    j += 1
                else:  # There was repetition within the sub-square.
                    print("Puzzle was not solved correctly.")
                    return

            j = 3
            k += 1

        j = 6
        k = 6
        l += 1

        while l < 9:
            test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while k <= 8:
                while j <= 8:
                    if user_grid[k][j] in test_list:
                        temp = user_grid[k][j]
                        test_list.remove(temp)
                        j += 1
                    else:  # There was repetition within the sub-square.
                        print("Puzzle was not solved correctly.")
                        return

                j = 6
                k += 1

            l += 1

        print("Puzzle Solved!")
        print("")
        for rows in user_grid:
            print(rows)
        print("")
        print("*************************************")


def game_start():
    """
    Function that starts and controls the game.
    """
    for rows in user_grid:               # Displays the user's current board.
        print(rows)
    print("")
    print("Replace any '0' with any integer 1-9.")
    print("To select a position, enter the positions row then column.")
    print("When prompted, enter the number (1-9) you would like to use.")
    print("")

    def r_req():
        """
        Function that request's the row for the player's number. Player can also enter 'ANSWER' and
        the function will pass the already correct answer to the board validation function to test the
        algorithm.
        """
        valid_input = False
        while valid_input is False:
            r_str = input("Please enter row number: ")
            if r_str == "ANSWER":
                valid_input = True
                game_end(answer_grid)       # Passes the already completed board to the checker function.
                r_req()
            if len(r_str) > 1:
                print("Invalid input")
            elif ord(r_str) < 49:
                print("Invalid input")
            elif ord(r_str) > 57:
                print("Invalid input")
            else:
                valid_input = True
        return int(r_str)

    def c_req():
        """
        Function that request's the column for the player's number.
        """
        valid_input = False
        while valid_input is False:
            c_str = input("Please enter column number: ")
            if len(c_str) > 1:
                print("Invalid input")
            elif ord(c_str) < 49:
                print("Invalid input")
            elif ord(c_str) > 57:
                print("Invalid input")
            else:
                valid_input = True
        return int(c_str)

    def v_req():
        """
        Function that request's the number the player wants to put in the board.
        """
        valid_input = False
        while valid_input is False:
            v_str = input("Please enter integer value: ")
            if len(v_str) > 1:
                print("Invalid input")
            elif ord(v_str) < 49:
                print("Invalid input")
            elif ord(v_str) > 57:
                print("Invalid input")
            else:
                valid_input = True
        return int(v_str)

    r = r_req()
    c = c_req()
    if original_grid[r-1][c-1] != 0:     # Determines if the chosen location has an 'original' number already placed.
        print("Invalid Input, Position already populated on original board.")
        game_start()
    v = v_req()
    user_grid[r-1][c-1] = v         # Places the player's numbered in the board.
    for row in user_grid:
        for element in row:
            if element == 0:        # Checks to see if all spaces have been used.
                game_start()
    game_end(user_grid)             # If all spaces are taken, runs the board validation algorithm.


game_start()
