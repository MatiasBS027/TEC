package conceptos;
import java.lang.Math;


public class Tiempo {
    int horas;
    int minutos;
    int segundos;

    public Tiempo(int horas, int minutos, int segundos) {
        this.horas = horas;
        this.minutos = minutos;
        this.segundos = segundos;
    }

    public Tiempo diferencia(Tiempo tiempo) {
        int misSegundos;
        int otrosSegundos;
        int resultado;
        int nuevaHoras;
        int nuevosMinutos;
        int residuo;

        misSegundos = this.horas * 3600 + this.minutos * 60 + this.segundos;
        otrosSegundos = tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos;
        resultado = Math.abs(misSegundos - otrosSegundos);
        nuevaHoras= resultado / 3600;
        residuo = resultado % 3600;
        nuevosMinutos = residuo / 60;
        residuo = residuo % 60;
        return new Tiempo(nuevaHoras, nuevosMinutos, residuo);
    }
    public int getHoras(){
        return horas;
    }

    public int getMinutos(){
        return minutos;
    }
    public int getSegundos(){
        return segundos;
    }

    public void setHoras(int horas) {
        this.horas = horas;
    }
    public void setMinutos(int minutos) {
        this.minutos = minutos;
    }
    public void setSegundos(int segundos) {
        this.segundos = segundos;
    }
}


