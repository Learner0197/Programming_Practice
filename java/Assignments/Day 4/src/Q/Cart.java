package Q;

public class Cart {
	private double totalBill;
	private int totalItems;

	public void addtoCart(Dessert d, int quantity){
		double cost = d.calculateprice(quantity);
		totalBill+=cost;
		totalItems++;
		System.out.println(quantity + " " + d.flavor + " " + "added tp cart. Cost:" + cost);
	}
	public void printBill(){
		System.out.println("Total Cart Value:" + totalBill);
		System.out.println("Total Cart items:" + totalItems);
	}
}
