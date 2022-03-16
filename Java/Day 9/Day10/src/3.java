public class Question3 {
    public static void main(String[] args) {
        int a,b;
        a= (int) (Math.random()*100000);
        b= (int) (Math.random()*100000);
        int sum=a+b;
        System.out.println("The numbers is="+a+", "+b);
        System.out.println("The sum is= "+sum);
        System.out.println("The difference is="+ (a-b));
        System.out.println("The product is= "+ (a*b));
        System.out.println("The average is= "+ (sum/2));
    }
}
