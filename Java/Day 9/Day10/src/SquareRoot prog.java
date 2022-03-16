import java.util.Scanner;

public class SquareRoot {
    public static void main(String[] args) {
        int num;
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number= ");
        num=scan.nextInt();
        System.out.println("The square root is = "+ Math.sqrt(num));
    }
}
