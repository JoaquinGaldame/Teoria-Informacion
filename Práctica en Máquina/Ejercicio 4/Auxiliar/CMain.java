package com.teoria.capacidadDeCanal;

import javax.swing.*;

public class CMain {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                JFrame ventana = new CapacidadForm();
                ventana.setVisible(true);
                ventana.setSize(700,400);
                ventana.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            }
        });


    }
}
