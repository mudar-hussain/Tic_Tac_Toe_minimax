/* Initial setup */
var game_board = [0,0,0,0,0,0,0,0,0]
var human = -1;
var computer = +1;



/* Checking wining situation */
function gameOver(state, player){
    var win_state = [
    [state[7],state[4],state[1]],
    [state[8],state[5],state[2]],
    [state[9],state[6],state[3]],
    [state[7],state[8],state[9]],
    [state[4],state[5],state[6]],
    [state[1],state[2],state[3]],
    [state[7],state[5],state[3]],
    [state[1],state[5],state[9]],
    ];

    for(var i = 0; i<8; i++){
        var filled = 0;
        for(var j = 0; j<3; j++){
            if(win_state[i][j]==player)
                filled++;
        }
        if(filled == 3) return true;
        }
    return false;
}


/* Checking wining situation */
function gameOverAll(state){
    return gameOver(state, human) || gameOver(state, computer);

}

/* Calculating number of empty cells*/
function emptyCells(state){
    var cells = [];
    for (var i = 1; i<=9; i++){
        if(state[i] == 0)
            cells.push(i);
    }
    return cells;
}

/* Main Function */
function mark(cell){
    var button = document.getElementById("restart");
    button.disabled = true;
    var conditionsToContinue = gameOverAll(game_board)==false && emptyCells(game_board).length > 0;

    if(!conditionsToContinue){
        if(setMove(cell.id,human)){
            cell.innerHTML = "X";
            if(conditionsToContinue){
                aiTurn();
            }
        }
    }



}