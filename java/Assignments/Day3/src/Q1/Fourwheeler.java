package Q1;

public class Fourwheeler extends Vehicle{
	protected static double insurancerate = 10;
	
	public Fourwheeler(int registrationno, String comp_name, String model, double price) {
		super(registrationno, comp_name, model, price);
	}
	@Override
	public double calculateInsurance() {
		return (double) (price * insurancerate)/100;
	}
	
	public void displayDetails() {
		System.out.println("Four-Wheeler\nModel: " + model + "\nRegistration no.: " + registrationno + "\nCompany name: " + comp_name + "\nPrice: Rs. " + price);
		//System.out.println("Model: " + model);
		//System.out.println("\nRegistration no.: " + registrationno);
		//System.out.println("\nCompany name: " + comp_name);
		//System.out.println("\nPrice: Rs. " + price);
	}
}
