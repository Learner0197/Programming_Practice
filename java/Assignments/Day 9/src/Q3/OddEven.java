package Q3;

public class OddEven {
    public static void main(String[] args) {
        Check ch = new Check();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i < 10; i+=2) {
                    ch.oddCheck(i);
                    try{
                        Thread.sleep(500);
                    }
                    catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 2; i < 10; i+=2) {
                    ch.eveCheck(i);
                    try{
                        Thread.sleep(500);
                    }
                    catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }
}
