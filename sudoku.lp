% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

#const n=3.
% Size of half the number of items in a sudoku row, column, and subgrid


sudoku(X, Y, N) :- initial(X, Y, N).
% Add all the initial box items to a sudoku set


{ sudoku(X, Y, N) : N = 1..n*n } = 1 :- X = 1..n*n, Y = 1..n*n.
% Generate all possible box coordinates with one number per box numbers with the initial box items included
:- sudoku(X, Y, N), sudoku(X', Y, N), X != X'.
% Remove box items with the same number in diffrent spots in the same row
:- sudoku(X, Y, N), sudoku(X, Y', N), Y != Y'.
% Remove box items with the same number in diffrent spots in the same column


subgrid(X, Y, G) :- X = 1..n*n, Y = 1..n*n, G = (((Y - 1) / n) + (((X - 1) / n) * n)) + 1.
% Define the subgrids so that each subgrid is enumerated starting from the top to the bottom and progressing from the left to the right of the full sudoku grid


sudoku(X, Y, N, G) :- sudoku(X, Y, N), G = (((Y - 1) / n) + (((X - 1) / n) * n)) + 1.
% Create a new set that describes the sudoku box items' locations, numbers, and subgrids


:- sudoku(X, Y, N, G), sudoku(X', Y', N, G), (X, Y) != (X', Y').
% Remove box items with the same number in different spots in the same subgrid


sudoku(X, Y, N) :- sudoku(X, Y, N, G).
% Transfer the sudoku solution to the initial sudoku atom of predicate three


%#show subgrid/3.
#show sudoku/3.
