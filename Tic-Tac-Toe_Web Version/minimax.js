console.log("Javascript - Tic-Tac-Toe");

/* Initial setup */
var game_board = [0,0,0,0,0,0,0,0,0,0]
var human = -1;
var computer = +1;

/* Evaluation of score */
function evaluate(state){
    if(gameOver(state,computer)) return +1;
    else if (gameOver(state,human)) return -1;
    else return 0;
}

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

/* Returns list of empty cells*/
function emptyCells(state){
    var cells = [];
    for (var i = 1; i<=9; i++){
        if(state[i] == 0)
            cells.push(i);
    }
    return cells;
}

/* check for valid Move */
function validMove(x){
    if(x == -1) return false;
    try{
        if(game_board[x] == 0) return true;
        else return false;
    }catch(e){
        return false;
    }
}



/*  AI for Computer's best move  */
function minimax(state, depth, player){
    if(depth == 0 || gameOverAll(state)){
        var score = evaluate(state);
        return [-1,score];
    }

    var best_move;
    if(player == computer){
        best_move = [-1, -1000];
    }else best_move = [-1, +1000];

    emptyCells(state).forEach(function (cell){
        state[cell] = player;
        var score = minimax(state, depth-1, -player);
        state[cell] = 0;
        score[0] = cell;
        if(player == computer){
            if(score[1] > best_move[1])
                best_move = score;
        }else{
            if(score[1] < best_move[1])
                best_move = score;
        }
    });
    return best_move;
}


/* Computer Turn */
function aiTurn(){
    var x;
    var move;
    var cell;
    if(emptyCells(game_board).length == 9){
        x = parseInt(Math.random()*10);

    }else{
        var y = minimax(game_board, emptyCells(game_board).length, computer);
        x = y[0];

    }
    if(x==0) x = x+1;
    console.log(x);
    if(validMove(x)){
        game_board[x] = computer;
        cell = document.getElementById(String(x));
        cell.innerHTML = "O";
    }
    console.log(game_board);
}


/* Main Function */
function mark(cell){
    console.log("Game started!")
    var button = document.getElementById("restart");
    button.disabled = true;
    var conditionsToContinue = gameOverAll(game_board)==false && emptyCells(game_board).length > 0;

    if(conditionsToContinue){
        if(validMove(cell.id)){
            game_board[cell.id] = human;
            cell.innerHTML = "X";
            if(conditionsToContinue){
                aiTurn();
            }
        }
    }



    if(emptyCells(game_board).length == 0 && !gameOverAll(game_board)){
        document.getElementById("result").innerHTML = "Game Draw - Let's play again";
    }
    if(gameOver(game_board,computer)){
        document.getElementById("result").innerHTML = "You loose! - Let's play again";
    }else if(gameOver(game_board,human)){
        document.getElementById("result").innerHTML = "You Win! - Let's play again";
    }
    if(emptyCells(game_board).length == 0 || gameOverAll(game_board)){
        button.value = "Restart";
        button.disabled = false;
    }
}

/* Restart Function */
function restart(button){
    if(button.value == "Play Computer"){
        button.disabled = true;
        aiTurn();
    }
    else{
        var htmlBoard;
        for(var i = 0; i<9; i++){
            game_board[i] = 0;
            htmlBoard = document.getElementById(String(i+1));
            htmlBoard.style.color = "#444";
            htmlBoard.innerHTML = "";
        }
        button.value = "Play Computer";
        document.getElementById("result").innerHTML = "";
    }
}