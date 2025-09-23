package Q;

public class Ice_cream extends Dessert {
	public Ice_cream(String flavor, double priceperpiece) {
		super(flavor, priceperpiece);
	}
	
	@Override
	public double calculateprice(int quantity) {
		return (double) (basePrice * quantity);
	}

}
