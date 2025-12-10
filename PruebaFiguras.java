package figuras;

public class PruebaFiguras {
    public static void main(String[] args) {
        Circulo figura1 = new Circulo(2);
        Rectangulo figura2 = new Rectangulo(1, 2);
        Cuadrado figura3 = new Cuadrado(3);
        TrianguloRectangulo figura4 = new TrianguloRectangulo(3, 5);
        Trapecio figura5 = new Trapecio(6, 4, 3, 3);

        System.out.println("Área del círculo: " + figura1.calcularArea());
        System.out.println("Perímetro del círculo: " + figura1.calcularPerimetro());
        System.out.println();

        System.out.println("Área del rectángulo: " + figura2.calcularArea());
        System.out.println("Perímetro del rectángulo: " + figura2.calcularPerimetro());
        System.out.println();

        System.out.println("Área del cuadrado: " + figura3.calcularArea());
        System.out.println("Perímetro del cuadrado: " + figura3.calcularPerimetro());
        System.out.println();

        System.out.println("Área del triángulo: " + figura4.calcularArea());
        System.out.println("Perímetro del triángulo: " + figura4.calcularPerimetro());
        figura4.determinarTipoTriangulo();
        System.out.println();

        System.out.println("Área del trapecio: " + figura5.calcularArea());
        System.out.println("Perímetro del trapecio: " + figura5.calcularPerimetro());
    }
}

