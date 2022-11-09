package Lab1;
import java.util.Scanner;
public class Task1 {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        procedura1();
            procedura2();
    }

    public static void procedura1(){
        int x, b;
        System.out.print("Введите значение x");
        x = scanner.nextDouble;
        System.out.print("Введите значение b");
        b = scanner.nextDouble;

        System.out.println(Y(x,b));
    }
    public static double Y(double x, double b) {
        return Math.log(x) - 5 + b * Math.cos(Math.pow(x, 4) - Math.log(52 * x)

    }
}
