# Sudoku-Solver

=======================================================================================

####Introduction

Creating a SUDOKU puzzle and solving is one of the famous problem solving question which we see in general coding competetions.
It can be solved using the Naive's Algorithm, but with a cost of 9**81 operations.
Backtracking algorithm comes into handy to solve this problem. It is a process of reverting back to the previous step or solution as soon as we determine that our
current solution cannot be continued into a complete one. I have used this principle of backtracking to implement the following algorithm.


I have built an application where we can fetch the puzzle from the API and hava a GUI application where we can solve this puzzle.
There is also going to be an auto solver which I am going to add going forward.

========================================================================================

#### Process


###Algorithm

Starting with an incomplete board:

=> Find some empty space
=> Attempt to place the digits 1-9 in that space
=> Check if that digit is valid in the current spot based on the current board
 a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
 b. If it is not valid, reset the square you just filled and go back to the previous step.
 
 Once the board is full by the definition of this algorithm we have found a solution

========================================================================================

#### GUI Implemetation

Implemented GUI using Pygame

 => Built the Pygame window
 => Added sudoku layouts, the grids
 => Populated the sudoku via an API to get these initial values
 
 
 
