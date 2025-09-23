package Q1;

public class Policy {

    public static void main(String[] args){

        Vehicle [] veh = new Vehicle[4];
        veh[0] = new Fourwheeler(3,"Tata","Nexon",1300000);
        veh[1] = new Twowheeler(4,"Honda","Activa",90000);
        veh[2] = new Fourwheeler(5,"Toyota","Fortuner",6000000);
        veh[3] = new Twowheeler(6,"Suzuki","Access",130000);

        for(Vehicle v: veh){

            System.out.println(v.comp_name + " " + v.model + " Vehicle Insurance: Rs." + v.calculateInsurance());
        }
    }
}
