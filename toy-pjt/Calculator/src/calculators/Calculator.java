package calculators;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;

public class Calculator {

	private JFrame frame;
	private JTextField txtDisplay;
	
	double firstnum;
	double secondnum;
	double result;
	String operations;
	String answer;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Calculator window = new Calculator();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Calculator() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 289, 421);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		txtDisplay = new JTextField();
		txtDisplay.setFont(new Font("±¼¸²", Font.BOLD, 22));
		txtDisplay.setHorizontalAlignment(SwingConstants.RIGHT);
		txtDisplay.setBounds(12, 10, 249, 50);
		frame.getContentPane().add(txtDisplay);
		txtDisplay.setColumns(10);

		
		// ------------- row 1 -------------
		JButton btnBack = new JButton("¡ç");
		btnBack.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String backspace = null;
				
				if(txtDisplay.getText().length() > 0) {
					StringBuilder strB = new StringBuilder(txtDisplay.getText());
					strB.deleteCharAt(txtDisplay.getText().length() - 1);
					backspace = strB.toString();
					txtDisplay.setText(backspace);
				}
				
				
			}
		});
		btnBack.setFont(new Font("±¼¸²", Font.BOLD, 14));
		btnBack.setBounds(22, 80, 50, 50);
		frame.getContentPane().add(btnBack);
		
		JButton btnC = new JButton("C");
		btnC.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				txtDisplay.setText(null);
			}
		});
		btnC.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnC.setBounds(82, 80, 50, 50);
		frame.getContentPane().add(btnC);
		
		JButton btnPer = new JButton("%");
		btnPer.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum = Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations = "%";
			}
		});
		btnPer.setFont(new Font("±¼¸²", Font.BOLD, 16));
		btnPer.setBounds(142, 80, 50, 50);
		frame.getContentPane().add(btnPer);
		
		JButton btnPl = new JButton("+");
		btnPl.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum = Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations = "+";
			}
		});
		btnPl.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnPl.setBounds(202, 80, 50, 50);
		frame.getContentPane().add(btnPl);
		
		// ------------- row 2 ------------- 
		JButton btn7 = new JButton("7");
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn7.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn7.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn7.setBounds(22, 140, 50, 50);
		frame.getContentPane().add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn8.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn8.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn8.setBounds(82, 140, 50, 50);
		frame.getContentPane().add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn9.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn9.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn9.setBounds(142, 140, 50, 50);
		frame.getContentPane().add(btn9);
		
		JButton btnMi = new JButton("-");
		btnMi.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum = Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations = "-";
			}
		});
		btnMi.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnMi.setBounds(202, 140, 50, 50);
		frame.getContentPane().add(btnMi);
		
		
		
		// ------------- row 3 -------------
		JButton btn4 = new JButton("4");
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn4.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn4.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn4.setBounds(22, 200, 50, 50);
		frame.getContentPane().add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn5.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn5.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn5.setBounds(82, 200, 50, 50);
		frame.getContentPane().add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn6.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn6.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn6.setBounds(142, 200, 50, 50);
		frame.getContentPane().add(btn6);
		
		JButton btnMul = new JButton("*");
		btnMul.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum = Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations = "*";
			}
		});
		btnMul.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnMul.setBounds(202, 200, 50, 50);
		frame.getContentPane().add(btnMul);
		
		
		// ------------- row 4 -------------
		JButton btn1 = new JButton("1");
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn1.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn1.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn1.setBounds(22, 260, 50, 50);
		frame.getContentPane().add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn2.getText();
				txtDisplay.setText(EnterNumber);
			}
		});btn2.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn2.setBounds(82, 260, 50, 50);
		frame.getContentPane().add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn3.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn3.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn3.setBounds(142, 260, 50, 50);
		frame.getContentPane().add(btn3);
		
		JButton btnDiv = new JButton("/");
		btnDiv.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum = Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations = "/";
			}
		});
		btnDiv.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnDiv.setBounds(202, 260, 50, 50);
		frame.getContentPane().add(btnDiv);
		
		
		
		// ------------- row 5 -------------
		JButton btnPM = new JButton("¡¾");
		btnPM.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double ops = Double.parseDouble(txtDisplay.getText());
				ops = ops * (-1);
				txtDisplay.setText(String.valueOf(ops));
			}
		});
		btnPM.setFont(new Font("±¼¸²", Font.BOLD, 18));
		btnPM.setBounds(22, 320, 50, 50);
		frame.getContentPane().add(btnPM);
		
		JButton btn0 = new JButton("0");
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String EnterNumber = txtDisplay.getText() + btn0.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn0.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btn0.setBounds(82, 320, 50, 50);
		frame.getContentPane().add(btn0);
		
		JButton btnDot = new JButton(".");
		btnDot.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				if (!txtDisplay.getText().contains(".")) {
					String EnterNumber = txtDisplay.getText() + btnDot.getText();
					txtDisplay.setText(EnterNumber);
				}
				
			}
		});
		btnDot.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnDot.setBounds(142, 320, 50, 50);
		frame.getContentPane().add(btnDot);
		
		JButton btnEq = new JButton("=");
		btnEq.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String answer;
				secondnum = Double.parseDouble(txtDisplay.getText());
				if (operations == "+") {
					result = firstnum + secondnum;
					answer = String.format("%.2f", result);
					txtDisplay.setText(answer);
				}
				
				else if (operations == "-") {
					result = firstnum - secondnum;
					answer = String.format("%.2f", result);
					txtDisplay.setText(answer);
				}
				
				else if (operations == "*") {
					result = firstnum * secondnum;
					answer = String.format("%.2f", result);
					txtDisplay.setText(answer);
				}
				
				else if (operations == "/") {
					result = firstnum / secondnum;
					answer = String.format("%.2f", result);
					txtDisplay.setText(answer);
				}
				
				else if (operations == "%") {
					int remain;
					remain = (int)(firstnum % secondnum);
					answer = String.format("%d", remain);
					txtDisplay.setText(answer);
				}
				
//				5. ¿¡¼­ = ¸¦ Å¬¸¯ÇßÀ» ¶§ .À» ¾ø¾Ö´Â ·ÎÁ÷À» ±¸ÇöÇÏ°í ½ÍÀ¸³ª ½ÇÆÐ
//				if (txtDisplay.getText().charAt(-1) == ".") {
//					txtDisplay.setText())
//				}
			}
		});
		btnEq.setFont(new Font("±¼¸²", Font.BOLD, 20));
		btnEq.setBounds(202, 320, 50, 50);
		frame.getContentPane().add(btnEq);
	}
}
