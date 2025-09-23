package Q;
import java.util.Scanner;
public class Store {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Cart cart = new Cart();
        boolean keepshopping = true;

        while(keepshopping){
            System.out.println("\n Dessert Menu:");
            System.out.println("1. Candy (per kg)");
            System.out.println("2. Cookie (per dozen)");
            System.out.println("3. Ice Cream (per piece)");
            System.out.println("4. Exit and Print Bill");
            System.out.println("Enter Choice");
            int choice = sc.nextInt();
            sc.nextLine();

            if(choice==4){
                keepshopping = false;
                break;
            }

            System.out.println("Enter the flavor");
            String flavor = sc.nextLine();
            System.out.println("Enter the price of the flavor");
            double price = sc.nextDouble();
            System.out.println("Enter the quantity");
            int quantity = sc.nextInt();

            Dessert d = null;
            switch(choice){
                case 1:
                    d = new Candy(flavor, price);
                    break;
                case 2:
                    d = new Cookie(flavor, price);
                    break;
                case 3:
                    d = new Ice_cream(flavor, price);
                    break;
                default:
                    System.out.println("Invalid Choice");
                    continue;                    
            }
        cart.addtoCart(d,quantity);
        }
    cart.printBill();
    }
}

