package Q1;


import java.util.Set;

public class Toys implements Comparable<Toys> {
    private int prodid;
    private String name;
    private double price;
    private Set<String> category;
    private int ageclass;
    private int purchaseyear;
    public Toys(int prodid, String name, double price, Set<String> category, int ageclass, int purchaseyear) {
        super();
        this.prodid = prodid;
        this.name = name;
        this.price = price;
        this.category = category;
        this.ageclass = ageclass;
        this.purchaseyear = purchaseyear;
    }

    public int getProdid() {
        return prodid;
    }

    public void setProdid(int prodid) {
        this.prodid = prodid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getAgeclass() {
        return ageclass;
    }

    public void setAgeclass(int ageclass) {
        this.ageclass = ageclass;
    }

    public Set<String> getCategory() {
        return category;
    }

    public void setCategory(Set<String> category) {
        this.category = category;
    }

    public int getPurchaseyear() {
        return purchaseyear;
    }

    public void setPurchaseyear(int purchaseyear) {
        this.purchaseyear = purchaseyear;
    }

    @Override
    public String toString(){
        return "Toy: " + name + "\nCategory: " + category + "\nAgeclass: " + ageclass + "\nPrice Rs.: " + price + "\nPurchaseyear: " + purchaseyear;
    }

    @Override
    public int compareTo(Toys o) {
        return this.getName().compareTo(o.getName());
    }

}
