// Nombre: Alexandra Ascanio
// Fecha: 2025
// Este programa muestra el factorial de los números del 1 al 13

public class Main {
    public static void main(String[] args) {

        // Creo un objeto de la clase Factorial para usar su método
        Factorial calc = new Factorial();

        // Recorro los números del 1 al 13
        for (int i = 1; i <= 13; i++) {

            // Llamo al método factorial enviando el número i
            int resultado = calc.factorial(i);

            // Muestro el número y su factorial
            System.out.println("Factorial de " + i + " = " + resultado);
        }
    }
}


