    /*
     * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
     * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
     */
    package aplication;
    import java.util.Scanner;

    /**
     *
     * @author Matias
     * carnee: 2025102376
     */
    public class Factorial {

        /**
         * @param args the command line arguments
         */
        public static void main(String[] args) {
            String keepGoing = "y";
            Scanner scanner = new Scanner(System.in);

            while (keepGoing.equals("y") || keepGoing.equals("Y")) {
                System.out.print("Ingrese un numero entero: ");
                int numero = scanner.nextInt();
                try {
                    System.out.println("Factorial ("+numero+") = "+ MathUtils.factorial(numero));
                } catch (IllegalArgumentException e) {
                    System.out.println("Error: " + e.getMessage());
                }
                System.out.print("Desea continuar? (y/n): ");
                keepGoing = scanner.next();
            }
        }
        public class MathUtils {
            //-----------------------------------------------
            // Retorna el factorial de un numero
            //-----------------------------------------------
            public static int factorial(int n) throws IllegalArgumentException {
                if (n < 0) {
                    throw new IllegalArgumentException("El factorial no está definido para números negativos");
                }
                if (n > 16) {
                    throw new IllegalArgumentException("El argumento debe ser menor o igual a 16 (desbordamiento aritmético)");
                }
                int fac = 1;
                for (int i = n; i > 0; i--) {
                    fac *= i;
                }
                return fac;
            }
        }
    }
