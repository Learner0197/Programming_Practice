package Q;

public class Cookie extends Dessert {
	public Cookie(String flavor, double priceperdozen) {
		super(flavor, priceperdozen);
	}
	
	@Override
	public double calculateprice(int quantity) {
		return (double) (basePrice * quantity)/12;
	}

}
