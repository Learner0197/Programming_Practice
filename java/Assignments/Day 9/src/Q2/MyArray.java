package Q2;

public class MyArray {

    public synchronized void PrintArray(int[] arr){
        for(int j=0;j<arr.length;j++){
            System.out.println(arr[j]);
        try {
            Thread.sleep(500);
        }  catch (InterruptedException e) {
            e.printStackTrace();
        }}
    }
}
