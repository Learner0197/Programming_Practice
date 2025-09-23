package Q1;

public abstract class Vehicle {

    protected int registrationno;
    protected String comp_name;
    protected String model;
    protected double price;

    public Vehicle(int registrationno, String comp_name, String model, double price) {
        this.registrationno = registrationno;
        this.comp_name = comp_name;
        this.model = model;
        this.price = price;
    }

    public abstract double calculateInsurance();
//    public abstract void displayInsuranceinfo();

}
