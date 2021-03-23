ReadMe for sudoku.py file

A sudoku game program with one board. The player can place valid inputs (integers 1-9), into valid locations
within the board that were not occupied by an 'original' number (numbers that were already placed on the original
board). When all the board locations are occupied, the program will run a validation function to see if the board is
correct. The board is correct if each row contains numbers 1-9 with none repeating, each column contains numbers 1-9
with none repeating, and each sub-square contains numbers 1-9 with none repeating.

The program will begin by displaying the board and asking the player for the row they would like to select. The player
can enter any integer 1-9 where 1 is the top row and 9 is the bottom row. Next, the program will ask the player to enter
the coloumn they would like to select. The player can enter any integer 1-9, where 1 is the leftmost column and 9 is the
rightmost colomn. Lastly the player will be asked to enter a value to fill the spot identified by their coordinates. If
the location identified by the player belongs to an 'original' number, the program will ask for new coordinates. The
player can however identify a number that they themselves has placed and change it.

To skip to the end of the game and check the algorithm, the player can enter 'ANSWER' for the program's first request
("Please enter row number: "), and the program will send the 'answer' board to the validation algorithm to check it.
This was implemented for easy testing, but was left in for grading. A copy of this ReadMe as well as
analysis/description of the determination algorithm are included on the accompanying PDF file.