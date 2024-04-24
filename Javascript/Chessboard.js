//Defining function for printing the chessboard.
function printChessboard(size) {
    let board = ''; //Initializing the variable.
    for (let row = 0; row < size; row = row + 1) { //Same nested forloop thing we had used in the pyramid project.
        for (let col = 0; col < size; col = col + 1) {
            if ((row + col) % 2 === 0) {//Determining where to put # or space;add space when it's even, otherwise #.
                board += ' ';
            } else {
                board += '#';
            }
            if (col === size - 1) {
                board += '\n';
            }
        }
    }
    console.log(board);
}

const size = 8; // Change this value to change the size of the chessboard
printChessboard(size);
