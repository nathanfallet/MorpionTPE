package fr.zabricraft.morpiontpe.logic;

public class Computer extends Player {
	
	int boardsize = 3;

	public void takeTurn(String[][] board, Human human) {

	    int vertical = 0;
	    int horizontal = 0;
	    int diagonal = 0;
	    boolean mademove = false;

	    // check if you can take a win horizontally
	    for(int i = 0; i<3; i++){

	        if(board[0][i].equals(board[1][i]) && board[0][i].equals(marker)){

	            if(board[2][i] != human.getMarker() && board[2][i] != marker){
	                board[2][i] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }

	    for(int i = 0; i<3; i++){

	        if(board[2][i].equals(board[1][i]) && board[2][i].equals(marker)){

	            if(board[0][i] != human.getMarker() && board[0][i] != marker){
	                board[0][i] = marker;
	                mademove = true;
	                return;
	            }

	        }


	    }



	    // check if you can take a win horizontally
	    for(int i = 0; i<3; i++){

	        if(board[i][0].equals(board[i][1]) && board[i][0].equals(marker)){

	            if(board[i][2] != human.getMarker() && board[i][2] != marker){
	                board[i][2] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }

	    for(int i = 0; i<3; i++){

	        if(board[i][2].equals(board[i][1]) && board[i][2].equals(marker)){

	            if(board[i][0] != human.getMarker() && board[i][0] != marker){
	                board[i][0] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }


	    // check if you can take a win diagonally bottom


	    if(board[0][0].equals(board[1][1]) && board[0][0].equals(marker)){

	        if(board[2][2] != human.getMarker() && board[2][2] != marker){
	            board[2][2] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[2][2].equals(board[1][1]) && board[2][2].equals(marker)){

	        if(board[0][0] != human.getMarker() && board[0][0] != marker){
	            board[0][0] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[0][0].equals(board[1][1]) && board[0][0].equals(marker)){

	        if(board[2][2] != human.getMarker() && board[2][2] != marker){
	            board[2][2] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[0][2].equals(board[1][1]) && board[0][2].equals(marker)){

	        if(board[2][0] != human.getMarker() && board[2][0] != marker){
	            board[2][0] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[2][0].equals(board[1][1]) && board[2][0].equals(marker)){

	        if(board[0][2] != human.getMarker() && board[0][2] != marker){
	            board[0][2] = marker;
	            mademove = true;
	            return;
	        }
	    }


	    // BLOCKS!!!! //

	    // check if you can block a win horizontally
	    for(int i = 0; i<3; i++){

	        if(board[0][i].equals(board[1][i]) && board[0][i].equals(human.getMarker())){
	            if(board[2][i] != marker && board[2][i] != human.getMarker()){
	                board[2][i] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }

	    for(int i = 0; i<3; i++){

	        if(board[2][i].equals(board[1][i]) && board[0][i].equals(human.getMarker())){

	            if(board[0][i] != marker && board[0][i] != human.getMarker()){
	                board[0][i] = marker;
	                mademove = true;
	                return;
	            }

	        }


	    }

	    // check if you can block a win vertically


	    for(int i = 0; i<3; i++){

	        if(board[i][0].equals(board[i][1]) && board[i][0].equals(human.getMarker())){

	            if(board[i][2] != marker && board[i][2] != human.getMarker()){
	                board[i][2] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }

	    for(int i = 0; i<3; i++){

	        if(board[i][2].equals(board[i][1]) && board[i][2].equals(human.getMarker())){

	            if(board[i][0] != marker && board[i][0] != human.getMarker()){
	                board[i][0] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }

	    for(int i = 0; i<3; i++){

	        if(board[2][i].equals(board[1][i]) && board[2][i].equals(human.getMarker())){

	            if(board[0][i] != marker && board[0][i] != human.getMarker()){
	                board[0][i] = marker;
	                mademove = true;
	                return;
	            }

	        }

	    }



	    // check if you can block a win diagonally 


	    if(board[0][0].equals(board[1][1]) && board[0][0].equals(human.getMarker())){

	        if(board[2][2] != marker && board[2][2] != human.getMarker()){
	            board[2][2] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[2][2].equals(board[1][1]) && board[2][2].equals(human.getMarker())){

	        if(board[0][0] != marker && board[0][0] != human.getMarker()){
	            board[0][0] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[0][0].equals(board[1][1]) && board[0][0].equals(human.getMarker())){
	        if(board[2][2] != marker && board[2][2] != human.getMarker()){
	            board[2][2] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[0][2].equals(board[1][1]) && board[0][2].equals(human.getMarker())){

	        if(board[2][0] != marker && board[2][0] != human.getMarker()){
	            board[2][0] = marker;
	            mademove = true;
	            return;
	        }
	    }

	    if(board[2][0].equals(board[1][1]) && board[2][0].equals(human.getMarker())){

	        if(board[0][2] != marker && board[0][2] != human.getMarker()){
	            board[0][2] = marker;
	            mademove = true;
	            return;
	        }
	    }




	    // make random move if above rules dont apply
	    int rand1 = 0;
	    int rand2 = 0;

	    while(!mademove){

	        rand1 = (int) (Math.random() * 3);
	        rand2 = (int) (Math.random() * 3);

	        if(board[rand1][rand2] != "x" && board[rand1][rand2] != "o"){
	            board[rand1][rand2] = marker;
	            mademove = true;        

	        }

	    }


	}

}
