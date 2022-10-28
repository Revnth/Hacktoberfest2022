// File name is calculateExpressionGame.java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Random;

class Game extends JFrame implements ActionListener{
	
	Container container = getContentPane();

	JLabel questionlabel = new JLabel("QUESTION : ");
	JTextField questiontext = new JTextField();
	JLabel answerlabel = new JLabel("ANSWER : ");
	JTextField answertext = new JTextField();
	JLabel presentscorelabel = new JLabel("PRESENT SCORE : ");
	JTextField presentscoretext = new JTextField();

	int result = 0;
	int score = -1;
	Timer gametimer;
	// GAME TIMER in seconds
	int start = 60;

	Game(){
		setLayoutManager();
		setLocationAndSize();
		addComponentsToContainer();
		addActionEvent();
		result = Calculate();
		Score();
		setTimer();
	}
	public void setLayoutManager() {
		container.setLayout(null);
	}
	public void setLocationAndSize() {
		questionlabel.setBounds(100, 100, 150, 30);
		questiontext.setBounds(100, 140, 150, 30);
		answerlabel.setBounds(100, 200, 150, 30);
		answertext.setBounds(100, 240, 150, 30);
		presentscorelabel.setBounds(100, 290, 150, 30);
		presentscoretext.setBounds(100, 330, 150, 30);
	}
	public void addComponentsToContainer() {
		container.add(questionlabel);
		container.add(questiontext);
		container.add(answerlabel);
		container.add( answertext);
		container.add(presentscorelabel);
		container.add( presentscoretext);
	}
	public void addActionEvent() {
		questiontext.setEditable(false);
		presentscoretext.setEditable(false);
		answertext.addActionListener(this);
		this.addWindowListener(new WindowAdapter() {
			@Override
			public void windowOpened(WindowEvent evt) {
				super.windowOpened(evt);
				answertext.requestFocus();
			}
		});
	}
	public void setTimer(){
		gametimer = new Timer(1000,this);
		gametimer.start();
	}
	@Override
	public void actionPerformed(ActionEvent e1) {
		start -= 1;
		if(start >= 0){
			try{
				String s = e1.getActionCommand();
				if(result == Integer.parseInt(s)){
					Score();
				}
				result = Calculate();
				answertext.setText(null);
			}
			catch(Exception e3){

			}
		}else{
			gametimer.stop();
			JOptionPane.showMessageDialog(this,"TIME IS UP. YOUR SCORE IS : " + score ,"SCORE",JOptionPane.PLAIN_MESSAGE);
			int option = JOptionPane.showConfirmDialog(this,"DO YOU WANT TO PLAY AGAIN ?","PLAY AGAIN SCORE : " + score,JOptionPane.YES_NO_OPTION,JOptionPane.INFORMATION_MESSAGE);
			if(option == JOptionPane.YES_OPTION){
				dispose();
				Game frame = new Game();
				frame.setTitle("PLAY");
				frame.setVisible(true);
				frame.setBounds(10,10,370,600);
				frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
				frame.setResizable(false);
			}
			else{
				dispose();
				Home frame = new Home();
				frame.setTitle("HOME");
				frame.setVisible(true);
				frame.setBounds(10,10,370,600);
				frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
				frame.setResizable(false);
			}
		}
	}

	int Calculate(){
		int num1 = new Random().nextInt(11); // 1 to 10
		int num2 = new Random().nextInt(11) + 1; // 0 to 10

		String operator = "+-/*%";
		int random_operator = new Random().nextInt(5);

		questiontext.setText("(" + num1 + ") " + operator.charAt(random_operator) + " (" + num2 + ")");

		return switch (operator.charAt(random_operator)) {
			case ('+') -> num1 + num2;
			case ('-') -> num1 - num2;
			case ('*') -> num1 * num2;
			case ('/') -> num1 / num2;
			case ('%') -> num1 % num2;
			default -> 0;
		};
	}

	void Score(){
		score += 1;
		presentscoretext.setText(" " +score + " ");
	}
}

class Home extends JFrame implements ActionListener{

	Container container = getContentPane();
	JLabel home = new JLabel("HOME",JLabel.CENTER);
	JButton playbutton = new JButton("PLAY");
	JButton exitbutton = new JButton("EXIT");

	Home(){
		setLayoutManager();
		setLocationAndSize();
		addComponentsToContainer();
		addActionEvent();
	}
	public void setLayoutManager(){
		// Content panes use
		// BorderLayout by default
		container.setLayout(null);
	}
	public void setLocationAndSize(){
		// position and size of the components
		// using setBounds(x,y,width,height)
		home.setBounds(125,20,125,30);
		// to display content or BackGround
		// behind a given component
		home.setOpaque(true);
		home.setBackground(Color.BLACK);
		home.setForeground(Color.WHITE);
		playbutton.setBounds(75,200,225,30);
		exitbutton.setBounds(75,250,225,30);
	}
	public void addComponentsToContainer(){
		container.add(home);
		container.add(playbutton);
		container.add(exitbutton);
	}
	public void addActionEvent(){
		// listen for changes on the object
		playbutton.addActionListener(this);
		exitbutton.addActionListener(this);
	}
	@Override
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == playbutton){
			// dispose() method clear
			// resources at each frame
			dispose();
			// to call the constructor of class Play
			Game frame = new Game();
			// Sets the title for this frame "PLAY"
			frame.setTitle("PLAY");
			// Component will be displayed on the screen
			frame.setVisible(true);
			// position and size of the frame
			// using setBounds(x,y,width,height)
			frame.setBounds(10,10,370,600);
			// application exits on close window
			// event from the operating system
			frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
			// user cannot re-size the frame
			frame.setResizable(false);
		}
		if(e.getSource() == exitbutton){
			// asks for confirmation from the user to exit or not
			int option = JOptionPane.showConfirmDialog(this,"Do You Really Want To Quit","Thank you", JOptionPane.YES_NO_OPTION,JOptionPane.PLAIN_MESSAGE);
			if(option == JOptionPane.YES_OPTION){
				dispose();
			}
		}
	}
}

public class MAN {
	public static void main(String[] arg){
		// to call the constructor of class Home
		Home frame = new Home();
		// Sets the title for this frame "HOME"
		frame.setTitle("HOME");
		// Component will be displayed on the screen
		frame.setVisible(true);
		// position and size of the frame
		// using setBounds(x,y,width,height)
		frame.setBounds(10,10,370,600);
		// application exits on close window
		// event from the operating system
		frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		// user cannot re-size the frame
		frame.setResizable(false);
	}
}
