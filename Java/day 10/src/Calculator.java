import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        int a,b;
        Scanner s=new Scanner(System.in);
        System.out.println("enter Number 1 :");
        a=s.nextInt();
        System.out.println("enter Number 2 :");
        b=s.nextInt();

        if(a>10000 && b>10000) {
            int sum,product,average,subtraction;
            sum=a+b;
            System.out.println("Sum :"+sum);
            product=a*b;
            System.out.println("Product :"+product);
            average=(a+b)/2;
            System.out.println("Average :"+average);
            subtraction=a-b;
            System.out.println("Subtraction :"+subtraction);
        }
        else {
            System.out.println("Your Number is less than 10000.");
        }
    }

}

