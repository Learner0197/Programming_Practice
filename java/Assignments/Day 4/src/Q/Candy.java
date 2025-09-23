package Q;

public class Candy extends Dessert {
	public Candy(String flavor, double priceperkg) {
		super(flavor, priceperkg);
	}
	
	@Override
	public double calculateprice(int quantity) {
		return (double) (basePrice * quantity)/1000;
	}

}
