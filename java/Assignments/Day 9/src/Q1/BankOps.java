package Q1;

public class BankOps {
    public static void main(String[] args) {
        Account acc = new Account(5000);
        new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<10;i++){
                    acc.withdraw(2000);

//                    try{
//                        Thread.sleep(3000);
//                    }catch(InterruptedException e){
//                        e.printStackTrace();
//                    }
                }
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<5;i++){
                    acc.deposit(3000);

                    try{
                        Thread.sleep(2000);
                    }catch(InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }).start();

    }
}
