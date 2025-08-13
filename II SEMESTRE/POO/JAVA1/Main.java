public class Main {
    public static void main(String[] args) {
        Lenguaje java = new Lenguaje("Java", "1995");
        Lenguaje python = new Lenguaje("Python", "1991");
        Lenguaje cSharp = new Lenguaje("C#", "2000");

        java.description();
        python.description();
        cSharp.description();
    }
}