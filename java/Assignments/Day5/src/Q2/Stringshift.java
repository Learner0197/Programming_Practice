package Q2;

import java.util.Scanner;

public class Stringshift {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String");
        String s = sc.nextLine();
        String n = "";
        char[] c = s.toCharArray();
        int i = 0;
        while(i<c.length-1){
            c[i] = c[i+1];
            i++;
        }
        c[i] = s.charAt(0);
        for(char j: c){
            n = n + j;
        }
        System.out.println(n);
    }
}
