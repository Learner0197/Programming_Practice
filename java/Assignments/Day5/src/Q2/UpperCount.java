package Q2;

import java.util.Scanner;

public class UpperCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String");
        String word = sc.nextLine();
        char[] c = word.toCharArray();
        int count = 0;
        for (char i : c) {
            if (i != ' ') {
                int n = i;
                if (n >= 65 && n <= 90) {
                    count++;
                }
            } else {
                continue;
            }
        }
        if(count == word.replace(" ", "").length()){
                System.out.println("Uppercase");
            }
        else{
            System.out.println("Not Uppercase");
        }
        }
    }

