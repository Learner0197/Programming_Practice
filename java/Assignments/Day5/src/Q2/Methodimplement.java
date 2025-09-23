package Q2;

public class Methodimplement {
    public boolean equals(String s1, String s2){
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        boolean check = false;
        for(int i = 0; i<c1.length; i++){
            if(c1[i]==c2[i]){
                check = true;
            }
            else{
                check = false;
                break;
            }
        }
        if(check == true){
            return true;
        }
        else{
            return false;
        }
    }

    public boolean equalsIgnoreCase(String s1, String s2){
        s1=s1.toLowerCase();
        s2=s2.toLowerCase();
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        boolean check = false;
        for(int i = 0; i<c1.length; i++){
            if(c1[i]==c2[i]){
                check = true;
            }
            else{
                check = false;
                break;
            }
        }
        if(check == true){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args){
        Methodimplement m = new Methodimplement();
        System.out.println(m.equals("AMAN", "aman"));
        System.out.println(m.equalsIgnoreCase("AMAN", "aman"));
    }
}
