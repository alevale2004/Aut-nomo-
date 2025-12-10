package figuras;

public class TrianguloRectangulo {
    private int base;
    private int altura;

    public TrianguloRectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }

    public double calcularArea() {
        return (base * altura) / 2.0;
    }

    public double calcularPerimetro() {
        return base + altura + calcularHipotenusa();
    }

    public double calcularHipotenusa() {
        return Math.sqrt((base * base) + (altura * altura));
    }

    public void determinarTipoTriangulo() {
        if (base == altura) {
            System.out.println("Es un triángulo isósceles.");
        } else if (base != altura) {
            System.out.println("Es un triángulo escaleno.");
        }
    }
}
