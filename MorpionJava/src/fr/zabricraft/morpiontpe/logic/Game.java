package fr.zabricraft.morpiontpe.logic;

public class Game {

	private int n = 3;
	public String[][] board = new String[n][n];
	
	public Game() {
		int x = 1;
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				board[i][j] = "" + (x);
				x++;
			}
		}
	}

	public String[][] getBoard() {
		return board;
	}

	public boolean hasWon() {
		// horizontal
		for (int i = 0; i < 3; i++) {
			if (board[i][0].equals(board[i][1]) && board[i][1].equals(board[i][2])) {
				return true;
			}
		}
		// vertical
		for (int i = 0; i < 3; i++) {
			if (board[0][i].equals(board[1][i]) && board[1][i].equals(board[2][i])) {
				return true;
			}
		}
		// diagonal
		if (board[0][0].equals(board[1][1]) && board[1][1].equals(board[2][2])
				|| board[2][0].equals(board[1][1]) && board[1][1].equals(board[0][2]))
			return true;
		return false;
	}

	public void printBoard() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				System.out.print("[" + board[i][j] + "]" + " ");

			}
			System.out.println();
		}
	}

}
