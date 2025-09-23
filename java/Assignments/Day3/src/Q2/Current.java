package Q2;

public class Current extends Account {
	protected static double maxWid = 50000;
	protected static double minDep = 50;
	
	public Current(int accno, String name, double bal) {
		super(accno, name, bal);		
	}
	@Override
	public boolean withdrawl(double w) {
		if(w>maxWid) {
			System.out.println("Transaction unsuccessful. Amount exceeds the limit.");
			return false;
		}
		else {
			System.out.println("Transaction successful.\nNew Balance:" + (bal-w));
			bal = bal-w;
			return true;
		}
	}
	
	@Override
	public boolean deposit(double d) {
		if(d<minDep) {
			System.out.println("Transaction unsuccessful. Minimum Deposit amount: Rs50.");
			return false;
		}
		else {	
			System.out.println("Transaction Successful.\nNew Balance:" + (bal+d));
			bal = bal+d;
			return true;
		}
	}
}
