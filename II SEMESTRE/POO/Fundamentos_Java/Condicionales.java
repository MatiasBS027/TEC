public class Main {
    public static void main(String[] args) {
        boolean autorized = false;
        if (autorized) {
            System.out.println("Acceso autorizado");
        } else {
            System.out.println("Acceso denegado");
        }
        int edad = 12;
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }
        String color = "rojo";
        switch (color) {
            case "rojo":
                System.out.println("El color es rojo");
                break;
            case "azul":
                System.out.println("El color es azul");
                break;
            default:
                System.out.println("Color no reconocido");
        }
    } 
}