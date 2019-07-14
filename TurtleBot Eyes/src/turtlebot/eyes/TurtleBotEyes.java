package turtlebot.eyes;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Toolkit;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import javax.swing.JComponent;
import javax.swing.JFrame;

/**
 *
 * @author James
 */
public class TurtleBotEyes extends JComponent {

    static int eyeRadius = 100;
    static int focusRadius = 20;

    static int imageWidth = 250;
    static int imageHeight = 250;

    static int displayWidth = 0;
    static int displayHeight = 0;

    //iris move time
    //iris will always take this amount of time (in seconds to move to their new position)
    static float irisMoveTime = (float) 1;

    //iris variables
    static float x = 0;
    static float y = 0;
    static float dx = 0;
    static float dy = 0;
    static float moveToX = 0;
    static float moveToY = 0;

    //iris focus variable (used to make it look like crabot is looking closer or further, bigger values for further); 
    static float focus = 0;
    static float moveToFocus = 0;
    static float dfocus = 0;

    //eye variables (the white part behind)
    static float ex = 0;
    static float ey = 0;
    static float edy = 0;
    static float edx = 0;

    //emotions 
    static int emotion = 0;

    static Graphics2D g2;

    static Image righteye = Toolkit.getDefaultToolkit().getImage("right eye.png");
    static Image lefteye = Toolkit.getDefaultToolkit().getImage("left eye.png");
    static Image happyEye = Toolkit.getDefaultToolkit().getImage("happy eye.png");
    static Image iris = Toolkit.getDefaultToolkit().getImage("basic iris.png");

    static TurtleBotEyes canvas = new TurtleBotEyes();

    /*
     *
     * @param args
     * @throws InterruptedException
     * @throws IOException
     */
    public static void main(String[] args) throws InterruptedException, IOException {

        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

//        window.setExtendedState(JFrame.MAXIMIZED_BOTH); //if you want fullscreen uncomment this
        window.setSize(800, 480);                       //if you want normal JFrame (easier for development on computer, resolution selected for LCD display intended) 
        window.setLocationRelativeTo(null);
        window.setUndecorated(true);
        window.setBackground(Color.black);
        window.getContentPane().add(canvas);
        window.setVisible(true);

        while (true) {
            calcPositions();
            canvas.repaint();
            displayWidth = window.getWidth();
            displayHeight = window.getHeight();
            readTextFile();
            Thread.sleep(10);
        }
    }

    /**
     * recalculates the position of the irises to determine how to move them,
     * where to move them, and how quickly they should move. should be called in
     * main loop to ensure smooth animation
     *
     */
    public static void calcPositions() {
        /*the position of the eyes are controlled by these velocities
           they are changed in such a way that the eyes will move faster the further
           they are away from the position they're moving too. aditionally they slow down exponentially
           as the moveto point is approached  
         */
        dx = (moveToX - x) / (irisMoveTime * 4);
        dy = (moveToY - y) / (irisMoveTime * 4);
        dfocus = 6 * (moveToFocus - focus) / (irisMoveTime * 10);

        //update xy positions
        x += dx;
        y += dy;
        focus += dfocus;
    }

    /**
     * Reads text file in same folder as executable, file can be modified while
     * this program is running allowing another program to control they eye
     * position without too much difficulty
     *
     * @throws IOException
     */
    public static void readTextFile() throws IOException {
        //default position values
        int xin = 90;
        int yin = 90;
        int fin = 0;
        String[] positions = {"0", "0", "0"};
        BufferedReader file = new BufferedReader(new FileReader("position.txt"));
        try {
            StringBuilder sb = new StringBuilder();
            String line = file.readLine();
            positions = line.split(",");
        } finally {
            file.close();
        }
        try {
            xin = Integer.parseInt(positions[0]);
            yin = Integer.parseInt(positions[1]);
            fin = Integer.parseInt(positions[2]);
            iris = Toolkit.getDefaultToolkit().getImage("basic iris.png");
        } catch (java.lang.ArrayIndexOutOfBoundsException e) {
            iris = Toolkit.getDefaultToolkit().getImage("error.png");
            canvas.repaint();
        }

        moveToDeg(xin, yin, fin);
    }

    /**
     * moves eyes to look at the degree given, function takes x and y degrees.
     * these are representative of the angle from the front of the screen 0
     * being center, -90 looking full right and 90 looking full left for the x
     * and -90 and 90 representing down and up for the y
     *
     * @param x_deg
     * @param y_deg
     */
    public static void moveToDeg(int x_deg, int y_deg) {
        moveTo(eyeRadius * Math.cos(((x_deg) * Math.PI) / 180), eyeRadius * Math.cos((y_deg * Math.PI) / 180), 0);
    }

    /**
     * moves eyes to look at degree given and at distance given (currently
     * unfinished)
     *
     * @param x_deg
     * @param y_deg
     * @param distance
     */
    public static void moveToDeg(int x_deg, int y_deg, int distance) {
        double _x, _y = 0;
        if (x_deg > 0) {
            _x = eyeRadius * Math.sin(((x_deg - 90) * Math.PI) / 180);
        } else {
            _x = eyeRadius * Math.sin(((x_deg - 90) * Math.PI) / 180);
        }

        if (y_deg > 0) {
            _y = eyeRadius * Math.sin(((y_deg - 90) * Math.PI) / 180);
        } else {
            _y = eyeRadius * Math.sin(((y_deg - 90) * Math.PI) / 180);
        }

        System.out.println(_x + " " + _y);
        double _distance = (distance);

        moveTo(_x, _y, _distance);
    }

    /**
     * passes values into the moveto integers.
     *
     * @param _x
     * @param _y
     * @param _focus
     */
    public static void moveTo(double _x, double _y, double _focus) {
        //pass directly into global variables
        moveToX = (float) _x;
        moveToY = (float) _y;
        moveToFocus = (float) _focus;
    }

    /**
     * paint method draws the screen, utilizes images declared at the top of the
     * class, these images can be modified to fit any style for crab bot
     *
     * @param g
     */
    public void paint(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;

        //fill background out with black 
        g.setColor(Color.black);
        g.fillRect(0, 0, displayWidth, displayHeight);

        //draw eyes, handle expressions (if we ever decide to do that) 
        g.drawImage(lefteye, 100, (int) (displayHeight - imageHeight) / 2, this);
        g.drawImage(righteye, displayWidth - imageWidth - 100, (int) (displayHeight - imageHeight) / 2, this);

        //draw iris (positioning identical to eye location but modified on x axis by focus variable)
        g.drawImage(iris, (int) (x + 100 - focus), (int) y + ((displayHeight - imageHeight) / 2), this);
        g.drawImage(iris, (int) (x + displayWidth - imageWidth - 100 + focus), (int) y + (displayHeight - imageHeight) / 2, this);

        g2.finalize();
    }

}
