package com.teoria.capacidadDeCanal;

public class CCanal {

    private double[] A; //Tengo que cargar los porcentajes de A porque despues debo mostrar sus valores de capacidad de canal
    private double[] B;
    private double[][] MatrizConjunta;
    private double entropiaA;
    private double entropiaB;
    private int filas;
    private int columnas;

    public double CalculoDeCapacidad(int fila, int columna, double[][] Matrix){
        filas = fila; //Cantidad de filas del canal
        columnas = columna; //Cantidad de columnas del canal
        A = new double[filas]; // Array de probabilidades de los simbolos de entrada ai
        B = new double[columnas]; //Array de probabilidades de los simbolos de salida bj
        double MaximaInfMutua = 0;
        double[] proMax = new double[filas]; // Array usado para inicializar las probabilidades ai para encontrar la capacidad

        MatrizConjunta = new double[filas][columnas]; // Matriz de las probabilidades conjuntas p(ai,bj)
        double resultadoParcial, resultadoTotal;
        double Aux;

        for(double k = 0.01; k < 1.0; k = k + 0.01){ // Mediante éstas itearaciones voy a ir modificando los valores de P(ai) para encontrar la capacidad

            proMax[0] = k; //Valor iniciar de P(a1) = 0.01, luego irá creciendo
            for (int i = 1; i < filas; i++){
                proMax[i] = (1.0 - proMax[0]) / (filas - 1); //Se ajustan los valores de las restantes P(ai) de modo que la sumatoria de 1
            }
            for (int j = 0; j < columnas; j++) //Saco las probabilidades de los simbolos de salida usando P(bj) = sum (P(ai) * P(bj/ai))
                B[j] = ProbabilidadBj(j, proMax, Matrix);


            for (int i = 0; i < fila; i++){  // Cargo la matriz de probabilidades conjuntas P(a,b)
                for (int j = 0; j < columna; j++){
                    MatrizConjunta[i][j] = proMax[i] * Matrix[i][j];
                }
            }

            resultadoParcial = 0; //Sumatoria (P(ai,bj) * log2 (P(ai,bj) / (P(bj) * P(ai)) )
            resultadoTotal = 0; // I(A,B)  = Sumatoria (resultadosParciles)
            for (int i = 0; i < filas; i++){
                for (int j = 0; j < columnas; j++)
                    resultadoParcial += MatrizConjunta[i][j] * (Math.log10(MatrizConjunta[i][j] / (proMax[i] * B[j])) / Math.log10(2));

                resultadoTotal += resultadoParcial;
            }

            Aux = resultadoTotal; //Calculo el maximo de todos los resultados totales (Informacion Mutua: I(A,B) )
            if (Aux > MaximaInfMutua){
                MaximaInfMutua = Aux;
                for (int i = 0; i < filas; i++)
                    A[i] = proMax[i];
                entropiaB = EntropiaX(B);
                entropiaA = EntropiaX(A);
            }
        }
        return MaximaInfMutua; // Este valor representa C: Capacidad de Canal
    }


    private static double EntropiaX(double[] Xi){ // H(A), H(B)

        double resultado = 0;
        for(int i = 0; i < Xi.length; i++){

            resultado += Xi[i] * (Math.log10(1/Xi[i]) / Math.log10(2));
        }
        return resultado;
    }

    private static double ProbabilidadBj(int j, double[] A, double[][] Matrix){ //P(bj) = sum (P(ai) * P(bj/ai))

        double resultado = 0;
        for (int i = 0; i < A.length; i++){
            resultado += A[i] * Matrix[i][j]; //sum (P(bj) = P(ai) * P(bj/ai))
        }
        return resultado;
    }

    /*
    private static double EntropiaCondicionalB_A(double[] A, double[][] Matriz){ //  H(B/A)
        double resultado = 0;
        for (int i = 0; i < A.length; i++ ){

            resultado += A[i] * EntropiaX(Matriz[i]);
        }
        return resultado;
    }*/

    public double[] getA(){ return A; }
    public double getEntropiaA() { return entropiaA; }
    public double getEntropiaB() { return entropiaB; }


}
