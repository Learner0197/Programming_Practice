package Q2;

public class Transac {
	
	public static void main(String[] args) {
		Savings S1 = new Savings(1, "Peter Parker", 9000);
		Current C1 = new Current(2, "Spider Man", 80000);
		S1.deposit(5000);
		S1.withdrawl(4500);
		S1.withdrawl(1000);
		C1.withdrawl(10000);
		C1.withdrawl(60000);
		C1.deposit(40);
		C1.deposit(10000);
		//Account.transaction(C1, S1, 10000);		
	}

}
