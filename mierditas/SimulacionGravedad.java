import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Random;

public class SimulacionGravedad extends JPanel implements ActionListener {
    private final ArrayList<Bola> bolas = new ArrayList<>();
    private final Timer timer = new Timer(16, this);

    public SimulacionGravedad() {
        Random rand = new Random();
        for (int i = 0; i < 20; i++) {
            bolas.add(new Bola(rand.nextInt(800), rand.nextInt(100), rand.nextInt(20) + 10));
        }
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, getWidth(), getHeight());
        for (Bola b : bolas) {
            g.setColor(Color.CYAN);
            g.fillOval((int) b.x, (int) b.y, b.radio, b.radio);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (Bola b : bolas) {
            b.actualizar(getHeight());
        }
        repaint();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Simulación de Gravedad en Java");
        SimulacionGravedad panel = new SimulacionGravedad();
        frame.add(panel);
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

class Bola {
    double x, y, vy = 0, gravedad = 0.5, friccion = 0.9;
    int radio;

    Bola(double x, double y, int radio) {
        this.x = x; this.y = y; this.radio = radio;
    }

    void actualizar(int altura) {
        vy += gravedad;
        y += vy;
        if (y + radio > altura) {
            y = altura - radio;
            vy *= -friccion;
        }
    }
}