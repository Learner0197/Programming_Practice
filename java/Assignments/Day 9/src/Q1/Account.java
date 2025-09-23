package Q1;

public class Account{
    private double balance;
    public Account(double balance){
        this.balance = balance;
    }
//    public double getBalance(){
//        return balance;

    public synchronized void withdraw(int amount) {
        while(this.balance < amount) {
            System.out.println("Insufficient funds. Wait for Deposit.");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.balance =  balance - amount;
        System.out.println("Withdrawn Successfully. New Balance: " + this.balance);
        notifyAll();
    }

    public synchronized void deposit(int amount) {
        this.balance =  balance + amount;
        System.out.println("Deposited Successfully. New Balance: " + this.balance);
        notifyAll();
    }
    }
