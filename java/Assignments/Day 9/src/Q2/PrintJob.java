package Q2;

public class PrintJob implements Runnable{

    MyArray array;
    int[] arr;

    public PrintJob(MyArray array, int[] arr){
        this.array = array;
        this.arr = arr;
    }

    @Override
    public void run() {
        array.PrintArray(arr);
            }
        }
