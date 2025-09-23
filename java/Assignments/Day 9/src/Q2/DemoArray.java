package Q2;

public class DemoArray {
    public static void main(String[] args) {
        MyArray a1 = new MyArray();

        int[] arr = {10,20,30,40,50,60,70,80,90,100};
        int[] arr2 = {10,20,30,40,50,60,70,80,90,100};

        new Thread(new PrintJob(a1,arr)).start();

        new Thread(new PrintJob(a1,arr2)).start();
        }
    }

