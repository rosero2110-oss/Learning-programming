/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.basic_cal1;

import java.util.Scanner;

/**
 *
 * @author Cristian
 */
public class Basic_cal1 {

    public static void main(String[] args) {
        float num1=0, num2=0, aadd=0;
        int opt=0;
        
        Scanner scanner;
        scanner = new Scanner (System.in);
        System.out.println("My basic calc");
        System.out.println("Enter first name: ");
        num1 = scanner.nextFloat();
        System.out.println("Enter second name: ");
        num2 = scanner.nextFloat();
        
        System.out.println(""
                + "(1). Addition"
                + "(2). Substraction"
                + "(3). Multiplication"
                + "(4). Division"
                + "(5). Averege"
                + "(6). all options"
                + ".::: Enter any option: ");
        opt = scanner.nextInt();
        
        switch (opt){
            case 1:
                //opt == 1
                System.out.println("Addition is: " + (num1 + num2));
                break;
            case 2:
                // opt == 2
                System.out.println("Substraction is: " + (num1 - num2));
                break;
            case 3:
                // opt == 3
                System.out.println("Multiplication is: " + (num1 * num2));
                break;
            case 4:
                // opt == 4
                System.out.println("Division is: " + (num1 / num2));
                break;
            case 5:
                // opt == 5
                System.out.println("Addition is: " + (num1 + num2) / 2);
                break;
            case 6:
                // opt == 6
                System.out.println("Addition is: " + (num1 + num2));
                System.out.println("Substraction is: " + (num1 - num2));
                System.out.println("Multiplication is: " + (num1 * num2));
                System.out.println("Division is: " + (num1 / num2));
                System.out.println("Addition is: " + (num1 + num2) / 2);
                break;
        }

        }    
    }

