
"function printChessboard(size) {
    let board = ''; "
//First step is to set up the function 'printChessboard' that takes single parameter 'size',pretty much the same as python.
    

    for (let row = 0; row < size; row++) {  
        for (let col = 0; col < size; col++) {
            if ((row + col) % 2 === 0) {
                board += ' ';
            } else {
                board += '#';
            }
            if (col === size - 1) {
                board += '\n';
            }
        }
    }
//Same nested forloop thing we had used in the pyramid project.The outer loop (for (let row = 0; row < size; row = row + 1)) iterates over each row, and the inner loop (for (let col = 0; col < size; col = col + 1)) iterates over each column within that row.

//Within the inner loop, I used the expression (row + col) % 2 === 0 to determine whether to add a space or a # character. If the sum of the row and column is even, add a space; else, add a #.The % operator is the modulo operator, which calculates the remainder of the division of the left parameters (row + col in this case) by the right parameters (2). Since we're using 2, this effectively checks whether the sum is an even number or an odd number. If the sum is even, the remainder when divided by 2 is 0; if it's odd, the remainder is 1.Finally, the === operator checks whether the result of the modulo operation ((row + col) % 2) is exactly equal to 0. This comparison returns true if the sum is even (and thus divisible by 2 with no remainder), and false if the sum is odd.

//After adding a character to the board string, I checked if the current column is at the end of the row (col === size - 1). If it is,add a newline character (\n) to move to the next line in the grid.So it can continue to print in the next following lines.

    
    
    console.log(board);
}
//Last step of the loop, printing out the chessboard.

const size = 8; 
printChessboard(size);

// Since we set the size variable to the desired value, and then we call the printChessboard function with this size to generate and print the chessboard.
