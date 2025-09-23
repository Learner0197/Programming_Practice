package Q1;

import java.util.Set;

public class ToyStream implements Comparable<ToyStream> {
    private int prodid;
    private String name;
    private double price;
    private String category;
    private String ageclass;
    private int purchaseyear;
    public ToyStream(int prodid, String name, double price, String category, String ageclass, int purchaseyear) {
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

    public String getAgeclass() {
        return ageclass;
    }

    public void setAgeclass(String ageclass) {
        this.ageclass = ageclass;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
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
    public int compareTo(ToyStream o) {
        return this.getName().compareTo(o.getName());
    }

}

