import java.util.Scanner;

public class FahrenheitToCelsius {
    public static void main(String[] args) {
        float Fahrenheit, Celsius;
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the Temperature in Fahrenheit= ");
        Fahrenheit = scan.nextFloat();
        Celsius  = ((Fahrenheit-32)*5)/9;
        System.out.println("Temperature in celsius is: "+Celsius);
    }
}
