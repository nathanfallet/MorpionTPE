package fr.zabricraft.morpiontpe;

import java.awt.Graphics;
import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.JPanel;

import fr.zabricraft.morpiontpe.logic.Computer;
import fr.zabricraft.morpiontpe.logic.Game;
import fr.zabricraft.morpiontpe.logic.Human;

public class Main {

	public static void main(String args[]) {
		new Main();
	}
	
	public Main() {
		JFrame frame = new JFrame();
		
		frame.setTitle("Morpion TPE");
		frame.setSize(640, 480);
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		GamePane pane = new GamePane();
		frame.setContentPane(pane);
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
		
		System.out.println("Welcome to Tickle Tackle Toe!!! :D");
		System.out.println();

		// creat markers
		String marker1 = "x";
		String marker2 = "o";
		boolean playAgain = true;

		Scanner s = new Scanner(System.in);

		// create player objects
		Human human = new Human();
		Computer computer = new Computer();

		while (playAgain) {
			// run board setup
			Game Setup = new Game();
			
			pane.update(Setup.board);

			human.setMarker("x");
			computer.setMarker("o");

			// determine who goes first
			int first = (int) (Math.random() * 2);

			boolean won = false;
			int turns = 0;

			if (first == 0) {
				System.out.println("You gots the winz!");
				System.out.println();
				while (!won) {
					human.takeTurn(Setup.getBoard());
					turns++;
					Setup.printBoard();
					if (Setup.hasWon()) {
						won = true;
						System.out.println("Congrats you won!");
					}
					if (turns == 9) {
						won = true;
						System.out.println("Its a bore draw!");
						break;
					}
					if (!won) {
						computer.takeTurn(Setup.getBoard(), human);
						turns++;
						System.out.println();
						Setup.printBoard();
						System.out.println();
						if (Setup.hasWon()) {
							won = true;
							System.out.println("You just got pwned by an A.I with an incomplete rule set. FACEPALM.");
						}
						if (turns == 9) {
							won = true;
							System.out.println("Its a bore draw!");
							break;
						}
					}

				} // close while 1
			} else {

				System.out.println("Computer goes first!");
				System.out.println();
				while (!won) {
					computer.takeTurn(Setup.getBoard(), human);
					turns++;
					Setup.printBoard();
					if (Setup.hasWon()) {
						won = true;
						System.out.println("You just got pwned by an A.I with an incomplete rule set. FACEPALM.");
					}
					if (turns == 9) {
						won = true;
						System.out.println("Its a draw!");
						break;
					}
					if (!won) {
						human.takeTurn(Setup.getBoard());
						turns++;
						System.out.println();
						Setup.printBoard();
						System.out.println();
						if (Setup.hasWon()) {
							won = true;
							System.out.println("You gots the winz!");
						}
						if (turns == 9) {
							won = true;
							System.out.println("Its a draw!");
							break;
						}
					}

				} // close while 2

			}

			System.out.println("Would you like to play again? Type 1 for yes or 2 to quit");
			System.out.println();
			if (s.nextInt() == 2) {
				playAgain = false;
			}

		}

	}
	
	private class GamePane extends JPanel {
		
		private String[][] board = new String[3][3];
		
		public void update(String[][] board) {
			this.board = board;
			repaint();
		}
		
		public void paintComponent(Graphics g) {
			
		}
		
	}

}
