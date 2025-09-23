package Q2;

public class Savings extends Account {
	protected static double minBal = 10000;
	
	public Savings(int accno, String name, double bal) {
		super(accno, name, bal);		
	}
	@Override
	public boolean withdrawl(double w) {
		if(bal<minBal) {
			System.out.println("Transaction unsuccessful. Account balance less than minimum balance.");
			System.out.println("Fine of Rs 500 deducted.\nNew Balance:" + (bal-500));
			bal = bal-500;
			return false;
		}
		else {
			System.out.println("Transaction successful.\nNew Balance:" + (bal-w));
			bal=bal-w;
			return true;
		}
	}
	
	@Override
	public boolean deposit(double d) {
		System.out.println("Transaction Successful.\nNew Balance:" + (bal+d));
		bal = bal+d;
		return true;
	}

}
