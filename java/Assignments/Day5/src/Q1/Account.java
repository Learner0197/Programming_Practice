package Q1;

import javax.security.auth.login.AccountNotFoundException;

public class Account {
    public static Account[] acc = new Account[4];
    private int accno;
    private String name;
    private double bal;

    public Account(int accno, String name, double bal) {
        this.accno = accno;
        this.name = name;
        this.bal = bal;
    }

    private double wamount;
    private double damount;


    public void withdrawl(int accno, double wamount) throws AccountNotFoundException, InsufficientBalanceException, NumberFormatException {
        boolean check = false;
        for (Account i : acc) {
            if (i.accno == accno) {
                check = true;
                if (wamount > i.bal) {
                    throw new InsufficientBalanceException("Withdrawal denied.Insufficient Balance.");
                } else {
                    i.bal = i.bal - wamount;
                    System.out.println("Withdrawal successful. Current balance: Rs." + i.bal);
                }
                break;
            }
        }
        if (check == false) {
            throw new AccountNotFoundException("Account not Found.");
        }
    }

    public void deposit(int accno, double damount) throws AccountNotFoundException, MaxDepLimitException, NumberFormatException {
        int deplim = 50000;
        boolean check = false;
        for (Account i : acc) {
            if (i.accno == accno) {
                check = true;
                if (damount > deplim) {
                    throw new MaxDepLimitException("Maximum Deposit Limit:" + deplim);
                } else {
                    i.bal = i.bal + damount;
                    System.out.println("Deposit successful. Current balance: Rs." + i.bal);
                }
                break;
            }
        }
        if (check == false) {
            throw new AccountNotFoundException("Account not Found.");
        }
    }

    public static void main(String[] args){
        acc[0] = new Account(1, "Jim", 50000);
        acc[1] = new Account(2, "John", 35000);
        acc[2] = new Account(3, "Jane", 76000);
        acc[3] = new Account(4, "Jack", 98000);

        Account handler = new Account(0,"Dummy", 0);

        try {
            handler.withdrawl(1, 51000);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
        try {
            handler.withdrawl(5, 51000);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
        try {
            handler.withdrawl(2, 10000);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
        try {
            handler.deposit(3, 51000);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
        try{
            handler.withdrawl(1,51000);
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }
}