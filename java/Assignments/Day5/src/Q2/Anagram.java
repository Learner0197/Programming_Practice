package Q2;


import java.util.Arrays;
import java.util.Scanner;

public class Anagram {

    private String word1;
    private String word2;

    public void CheckAnagram() {
        System.out.print("Enter word1: ");
        Scanner sc=new Scanner(System.in);
        String word1=sc.nextLine();
        word1 =word1.toLowerCase();
        System.out.print("Enter word2: ");
        String word2=sc.nextLine();
        word2 =word2.toLowerCase();
        String[] w1 = word1.split("");
        String[] w2 = word2.split("");

        Arrays.sort(w1);
        Arrays.sort(w2);
        if(Arrays.equals(w1, w2)) {
            System.out.println("Anagram");
        }
        else{
            System.out.println("Not Anagram");
        }
    }

    public static void main(){
        Anagram an=new Anagram();
        an.CheckAnagram();
    }


}
