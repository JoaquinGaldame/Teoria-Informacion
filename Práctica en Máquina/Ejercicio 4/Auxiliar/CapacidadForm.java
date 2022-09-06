package com.teoria.capacidadDeCanal;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CapacidadForm  extends JFrame{
    private JPanel panel1;
    private JTextField txtFilas;
    private JButton validarButton;
    private JButton calcularButton;
    private JButton salirButton;
    private JTable table1;
    private JTextField txtColumnas;
    private JLabel txtMensaje;
    private JLabel lblCapacidad;
    private JLabel lblPa1;
    private JLabel lblPa2;
    private JLabel lblPa3;
    private JLabel lblPa4;
    private JLabel lblHA;
    private JLabel lblHB;
    int R, C;

    public CapacidadForm(){
        super("Capacidad de Canal");
        setContentPane(panel1);
        salirButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                System.exit(0);
            }
        });
        validarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String sFilas = txtFilas.getText();
                String sColumnas = txtColumnas.getText();
                if (sFilas.length() != 0 && sColumnas.length() != 0){
                       R = Integer.parseInt(sFilas);
                       C = Integer.parseInt(sColumnas);
                       if ((R >= 2 && R <= 4)&&(C >= 1 && C <= 10)){
                           DefaultTableModel tableModel = new DefaultTableModel(R, C);
                           table1.setModel(tableModel);
                       }
                       else txtMensaje.setText("El valor de R no es valido (debe ser entre 2 y 4 y columnas entre 1 y 10)");
                }
                else txtMensaje.setText("Debe ingresar Valores de filas y columas validos");

            }
        });

        calcularButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                CCanal ce = new CCanal();
                double[][] Matriz = new double[R][C];
                int i, j;
                for (i = 0; i < R; i++){
                    for (j = 0; j < C; j++){
                        Matriz[i][j] = Double.parseDouble(table1.getValueAt(i,j).toString());
                    }
                }
                lblCapacidad.setText(Double.toString(ce.CalculoDeCapacidad(R, C, Matriz)));
                lblHA.setText(Double.toString(ce.getEntropiaA()));
                lblHB.setText(Double.toString(ce.getEntropiaB()));
                double[] Resultados = ce.getA();
                switch (R){
                    case 2:
                        lblPa1.setText(Double.toString(Resultados[0]));
                        lblPa2.setText(Double.toString(Resultados[1]));
                        lblPa3.setText("");
                        lblPa4.setText("");
                            break;
                    case 3:
                        lblPa1.setText(Double.toString(Resultados[0]));
                        lblPa2.setText(Double.toString(Resultados[1]));
                        lblPa3.setText(Double.toString(Resultados[2]));
                        lblPa4.setText("");
                        break;
                    case 4:
                        lblPa1.setText(Double.toString(Resultados[0]));
                        lblPa2.setText(Double.toString(Resultados[1]));
                        lblPa3.setText(Double.toString(Resultados[2]));
                        lblPa4.setText(Double.toString(Resultados[3]));
                        break;
                }
            }
        });
    }
}
