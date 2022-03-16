import java.util.Scanner;
public class LeapYear {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter Year :");
        int year=s.nextInt();
        String isleap=(year%4==0 && year%100!=0)?"Leap Year" :"Non-leap Year";
        System.out.println(year+" is"+isleap);

    }

}
