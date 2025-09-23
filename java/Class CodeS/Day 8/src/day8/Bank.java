package day8;

public class Bank {

    public static void main(String[] args) {
        WithdrawJob job = new WithdrawJob();
        Thread h =  new Thread(job);
        Thread w =  new Thread(job);
        h.setName("Husband");
        w.setName("Wife");

        h.start();
        w.start();
    }
}
