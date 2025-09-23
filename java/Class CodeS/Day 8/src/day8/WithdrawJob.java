package day8;

public class WithdrawJob implements Runnable{
    Account acc;

    public WithdrawJob(){
        acc = new Account(200000);
    }

    public synchronized void withdraw(int amount){
        if(acc.getBalance() > amount){
            System.out.println(Thread.currentThread().getName() + "is ready to withdraw");
            System.out.println(Thread.currentThread().getName() + "goes to sleep");

            try{
                Thread.sleep(2000);
            } catch(InterruptedException e){
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "wakes up");
            acc.withdraw(amount);
            System.out.println("Transaction successful for" + Thread.currentThread().getName());
            System.out.println("Balance: " + acc.getBalance());
        }
        else{
            System.out.println("Insufficient funds");
        }
    }
    @Override
    public void run(){
        for(int i=0; i<3; i++){
            withdraw(5000);
        }
    }
}
