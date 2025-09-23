package Q;

public abstract class Dessert {
	protected String flavor;
	protected double basePrice;
	
	public Dessert(String flavor, double basePrice) {
		this.flavor = flavor;
		this.basePrice = basePrice;
	}	
	public abstract double calculateprice(int quantity);
}
