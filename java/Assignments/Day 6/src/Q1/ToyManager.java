package Q1;

import java.util.*;
import java.util.Map.Entry;

public class ToyManager {

    public static List<Toys> toysList(){
        List<Toys> toysList = new ArrayList<>();
        Set<String> c1 = new TreeSet<>();
        c1.add("Educational");
        c1.add("Musical");
        Set<String> c2 = new TreeSet<>();
        c2.add("Sports");
        c2.add("Battery Operated");
        Set<String> c3 = new TreeSet<>();
        c3.add("Babies");
        c3.add("Musical");
        Set<String> c4 = new TreeSet<>();
        c4.add("Sports");
        c4.add("Outdoors");
        Set<String> c5 = new TreeSet<>();
        c5.add("Arcade");
        c5.add("Simulation");
        toysList.add(new Toys(1,"Piano",10000.00,c1,12,2021));
        toysList.add(new Toys(2,"RC Car",1500.00,c2,8,2024));
        toysList.add(new Toys(3,"Music Plushie",2000.00,c3,2,2024));
        toysList.add(new Toys(4,"Xylophone",1000.00,c1,8,2022));
        toysList.add(new Toys(5,"Cricket Set",5000.00,c4,10,2024));
        toysList.add(new Toys(6,"Monopoly",800.00,c5,12,2023));
        return toysList;
    }

    public static void addToy(List<Toys> toysList, Toys toys){
        toysList.add(toys);
    }

    public static void printList(List<Toys> toysList) {
        for (Toys toys : toysList) {
            System.out.println(toys);
        }
    }

    public static List<Toys> filterbyCategory(List<Toys> toysList, String cat){
            List<Toys> byCategory = new ArrayList<>();
            for(Toys toys:toysList){
                if(toys.getCategory().contains(cat)){
                    byCategory.add(toys);
                }
            }
            return byCategory;
        }


    public static List<Toys> searchbyProdID(List<Toys> toysList, int pid) {
        List<Toys> byProdID = new ArrayList<>();
        for (Toys toys : toysList) {
            byProdID.add(toys);
        }
        Collections.sort(byProdID, new IdComparator());
        int found = Collections.binarySearch(byProdID, new Toys(pid, null, 0, null, 0, 0), new IdComparator());
        System.out.println("found: " + found);
        return byProdID;
    }

    public static List<Toys> filterbyPrice(List<Toys> toysList, int lowerp, int  upperp) {
        List<Toys> byPrice = new ArrayList<>();
        for(Toys toys:toysList){
            if(toys.getPrice()>=lowerp && toys.getPrice()<=upperp){
                byPrice.add(toys);
            }
        }
        return byPrice;
    }

    public static List<Toys> filterbyAge(List<Toys> toysList, int lowera, int  uppera) {
        List<Toys> byAge = new ArrayList<>();
        for(Toys toys:toysList){
            if(toys.getAgeclass()>=lowera && toys.getAgeclass()<=uppera){
                byAge.add(toys);
            }
        }
        return byAge;
    }

    public static List<Toys> sortbyPrice(List<Toys> toysList) {
        List<Toys> byPrice = new ArrayList<>();
        for (Toys toys : toysList) {
            byPrice.add(toys);
        }
        Collections.sort(byPrice, new PriceComparator());
        return byPrice;
    }

    public static List<Toys> sortbyName(List<Toys> toysList) {
        List<Toys> byName = new ArrayList<>();
        for (Toys toys : toysList) {
            byName.add(toys);
        }
        Collections.sort(byName, new NameComparator());
        return byName;
    }

    public static List<Toys> filterOutOld(List<Toys> toysList) {
        List<Toys> byYear = new ArrayList<>();
        for(Toys toys:toysList){
            if(toys.getPurchaseyear() < 2024){
                byYear.add(toys);
            }
        }
        return byYear;
    }

    public static Map<String, Set<String>> mapbyCategory(List<Toys> toysList) {
        Map<String, Set<String>> byCategory = new TreeMap<>();
        for (Toys toys : toysList) {
            byCategory.put(toys.getName(), toys.getCategory());
        }
        return byCategory;

    }

    public static void main(String[] args){
        List<Toys> Stock = ToyManager.toysList();
        ToyManager.printList(Stock);

        List<Toys> Cat = ToyManager.filterbyCategory(Stock, "Battery Operated");
        ToyManager.printList(Cat);

        List<Toys> Search = ToyManager.searchbyProdID(Stock,3);
        ToyManager.printList(Search);

        List<Toys> Price = ToyManager.filterbyPrice(Stock, 1000, 5000);
        ToyManager.printList(Price);

        List<Toys> Ageclass = ToyManager.filterbyAge(Stock, 10, 15);
        ToyManager.printList(Ageclass);

        List<Toys> SortPrice = ToyManager.sortbyPrice(Stock);
        ToyManager.printList(SortPrice);

        List<Toys> SortName = ToyManager.sortbyName(Stock);
        ToyManager.printList(SortName);

        List<Toys> OldFilter = ToyManager.filterOutOld(Stock);
        ToyManager.printList(OldFilter);

        Map<String, Set<String>> CategoryGroup = ToyManager.mapbyCategory(Stock);
        for(Entry<String, Set<String>> entry:CategoryGroup.entrySet()){
            System.out.println(entry.getKey() + ":" + entry.getValue());
        }
    }
}
