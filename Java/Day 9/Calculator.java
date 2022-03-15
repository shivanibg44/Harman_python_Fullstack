package com.harman.project1;
import org.w3c.dom.ls.LSOutput;
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Addition add=new Addition();
        Substraction sub=new Substraction();
        Multiplication mul=new Multiplication();
        Division Div=new Division();
        Integer X,Y,addresult,subresult,multiplyresult,divisionresult;
        Scanner input=new Scanner(System.in);
        System.out.println("num1:");
        X=input.nextInt();
        System.out.println("num2");
        Y=input.nextInt();
        addResult=add.Addnumber(X,Y);
        System.out.println(addesult);
        subresult=sub.Subtraction(X,Y);
        System.out.println(subresult);
        multiplyresult= mul.Multiplication(X,Y);
        System.out.println(multiplyresult);
        divisionresult= Div.Division(X,Y);
        System.out.println(divisionresult);




    }
}
