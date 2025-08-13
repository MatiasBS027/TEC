import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> animals = new ArrayList<String>();
        animals.add("Perro");
        animals.add("Gato");
        animals.add("Pájaro");
        animals.add("Pez");
        animals.add("Conejo");
        animals.add("Tortuga");

        for (String animal : animals) {
            System.out.println(animal);
        }
    } 
}