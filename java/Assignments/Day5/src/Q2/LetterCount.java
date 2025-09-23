package Q2;

import java.util.Arrays;
import java.util.Scanner;

public class LetterCount {
    private String inp;
    private int capital;
    private int lower;
    private int specialchar;
    private int num;


    public void CountLetters(){
        System.out.print("Enter sentence: ");
        Scanner sc=new Scanner(System.in);
        inp = sc.nextLine();
        inp = inp.replace(" ","");
        char[] w3=inp.toCharArray();
        Arrays.sort(w3);
        capital = 0;
        lower = 0;
        specialchar = 0;
        num = 0;
        for(int i=0;i<w3.length;i++){
            if(w3[i] > 64 && w3[i] < 91){
                capital++;
            }
            else if(w3[i] > 97 && w3[i] < 123){
                lower++;
            }
            else if(w3[i] > 47 && w3[i] < 58){
                num++;
            }
            else{
                specialchar++;
        }
        }

    System.out.print("Uppercase letters: " + capital + "\nLowercase letters: " + lower + "\nNumbers: " + num+ "\nSpecial characters: " + specialchar);




    }

    public static void main(String[] args) {
        LetterCount l=new LetterCount();
        l.CountLetters();
    }
}
