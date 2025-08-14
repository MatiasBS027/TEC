public class Libro {
    String titulo;
    String autor;

    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor; 
    }

    public void description() {
        System.out.println(this.titulo + " by " + this.autor);
    }
}