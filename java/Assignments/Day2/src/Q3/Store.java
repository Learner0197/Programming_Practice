package Q3;

public class Store {
	Product[] product;
	
	public Store(Product[] product) {
		this.product = product;
		
	}
	
	public void displayProduct() {
		for(int l=0;l<product.length;l++) {
			System.out.println(product[l]);
		}
	}

}
