public class Lenguaje {
    String nombre;
    String anno;

    public Lenguaje() {}

    public Lenguaje(String nombre, String anno) {
        this.nombre = nombre;
        this.anno = anno; 
    }

    public void description() {
        System.out.println(this.nombre + " fue creado en " + this.anno);
    }
}