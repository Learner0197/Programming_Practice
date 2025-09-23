package Q2;

public abstract class Account {
	protected int accno;
	protected String name;
	protected double bal;
	
	public Account(int accno, String name, double bal) {
		this.accno = accno;
		this.name = name;
		this.bal = bal;
	}
	
	public abstract boolean withdrawl(double wamount);
	public abstract boolean deposit(double damount);
	
	public static void transaction(Account sender, Account receiver, double amount) {
		if(sender.withdrawl(amount)) {
			if(receiver.deposit(amount)) {
				System.out.println("Transaction Completed");
//				sender.withdrawl(amount);
//				receiver.deposit(amount);
			}
			else {
				System.out.println("Error from receiver's end");
			}
		}
		else {
			System.out.println("Error on Sender's end.");
		}
	}
}
