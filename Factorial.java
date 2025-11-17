// Clase que contiene el método para calcular el factorial
public class Factorial {

    // Método que recibe un número y devuelve su factorial
    public int factorial(int n) {

        int total = 1; // Aquí se va acumulando la multiplicación

        // Multiplico desde 1 hasta n
        for (int i = 1; i <= n; i++) {
            total = total * i;
        }

        return total; // Devuelvo el resultado
    }
}


