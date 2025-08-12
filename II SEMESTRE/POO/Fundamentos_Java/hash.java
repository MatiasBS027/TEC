import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, String> jugadores = new HashMap<Integer, String>(); // Se crea un HashMap de enteros a cadenas
        jugadores.put(1, "Lionel Messi"); // Se añade un jugador con ID 1
        jugadores.put(2, "Cristiano Ronaldo"); // Se añade un jugador con ID
        System.out.println(jugadores.get(1));
        System.out.println(jugadores); // Se imprime el nombre del jugador con ID 2
    } 
}