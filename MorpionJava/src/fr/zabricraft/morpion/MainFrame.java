package fr.zabricraft.morpion;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class MainFrame extends JFrame {
	
	public static void main(String args[]) {
		try {
			new MainFrame();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	private Image iconX;
	private Image iconO;
	private String[][] board = {{"", "", ""}, {"", "", ""}, {"", "", ""}};
	
	public MainFrame() throws IOException {
		iconX = ImageIO.read(new File("/Users/zabricraft/Desktop/x.jpg"));
		iconO = ImageIO.read(new File("/Users/zabricraft/Desktop/o.jpg"));
		
		setTitle("IA Morpion");
		setSize(640, 480);
		setResizable(false);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setContentPane(new MainPane());
		setVisible(true);
		
		board[1][1] = "x";
		
		new Thread(new Runnable() {
			@Override
			public void run() {
				
			}
		}).start();
	}
	
	public Result getResult() {
		
		return Result.NULL;
	}
	
	
	
	private enum Result {
		NULL, X, O, TIE;
	}

	private class MainPane extends JPanel {
		
		public void paint(Graphics g) {
			g.setColor(Color.BLACK);
			g.fillRect(0, 0, getWidth(), getHeight());
			for(int i = 0; i < 3; i++) {
				for(int j = 0; j < 3; j++) {
					if (!board[i][j].isEmpty()) {
						g.drawImage(board[i][j].equals("x") ? iconX : iconO, i*getWidth()/3, j*getHeight()/3, getWidth()/3, getHeight()/3, this);
					}
				}
			}

			g.setColor(Color.WHITE);
			g.drawLine(0, getHeight()/3, getWidth(), getHeight()/3);
			g.drawLine(0, getHeight()/3*2, getWidth(), getHeight()/3*2);
			g.drawLine(getWidth()/3, 0, getWidth()/3, getHeight());
			g.drawLine(getWidth()/3*2, 0, getWidth()/3*2, getHeight());
		}
		
	}
	
}
