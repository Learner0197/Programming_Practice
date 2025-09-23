package Q3;

public class Product {
	private int prodid;
	private String name;
	private int price;
	private int count = 1;
	public Product(int prodid, String name, int price) {
		this.prodid = count++;
		this.name = name;
		this.price = price;
	}
	
	
}
