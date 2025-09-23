package Q1;

import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ToyManager {
    public static List<ToyStream> createToysList(){
        List<ToyStream> list = new ArrayList<>();

        list.add(new ToyStream(1, "Piano", 10000.00, "Musical", "3+", 2021));
        list.add(new ToyStream(2, "Xylophone", 5000.00, "Musical", "3+", 2024));
        list.add(new ToyStream(3, "Cricket Set", 4000.00, "Sports", "12+", 2025));
        list.add(new ToyStream(4, "Football", 1000.00, "Sports", "12+", 2024));
        list.add(new ToyStream(5, "Alphabet Magazines", 500.00, "Educational", "5+", 2021));
        list.add(new ToyStream(6, "RC Car", 10000.00, "Battery Operated", "15+", 2024));

        return list;
    }

    public static void main(String[] args) {
        List<ToyStream> list = createToysList();
        Stream<ToyStream> stream = list.stream();

        System.out.println("Toys Stock:");
        stream.forEach(System.out::println);

        stream = list.stream();
        Predicate<ToyStream> byCat = (s) -> s.getCategory().equals("Musical");
        System.out.println("\nToys of Musical Category:");
        stream.filter(byCat).forEach(System.out::println);

        stream = list.stream();
        Predicate<ToyStream> byPrice = (s) -> s.getPrice()>=500 && s.getPrice()<=1000.00;
        System.out.println("\nToys with price between 500 and 1000.00:");
        stream.filter(byPrice).forEach(System.out::println);

        stream = list.stream();
        Comparator<ToyStream> bypricecategory = Comparator.comparing(ToyStream::getCategory).thenComparing(ToyStream::getPrice);
        System.out.println("\nToys with sorted toys price and category wise");
        stream.sorted(bypricecategory).forEach(System.out::println);

        stream = list.stream();
        Predicate<ToyStream> byOldStock = (s) -> s.getPurchaseyear() < 2024;
        System.out.println("\nToys older than a year:");
        stream.filter(byOldStock).forEach(System.out::println);

        stream = list.stream();
        Map<String, Long> byCategory = stream.collect(Collectors.groupingBy(ToyStream::getCategory, Collectors.counting()));
        System.out.println("\nToys with sorted by category and count of toys in each category:");
        byCategory.forEach((k,v)->System.out.println(k+": "+v));

        stream = list.stream();
        Map<String, Long> byAge = stream.collect(Collectors.groupingBy(ToyStream::getAgeclass, Collectors.counting()));
        System.out.println("\nToys sorted by age group:");
        byAge.forEach((k,v)->System.out.println(k+": "+v));

        stream = list.stream();
        Map<String, Optional<ToyStream>> byCatMin = stream.collect(Collectors.groupingBy(ToyStream::getCategory,Collectors.minBy(Comparator.comparing(ToyStream::getPrice))));
        System.out.println("\nLeast expensive toy in each category:");
        byCatMin.forEach((k,v)->System.out.println(k+": "+v));
        stream = list.stream();
        Map<String, Optional<ToyStream>> byCatMax = stream.collect(Collectors.groupingBy(ToyStream::getCategory,Collectors.maxBy(Comparator.comparing(ToyStream::getPrice))));
        System.out.println("\nMost expensive toy in each category:");
        byCatMax.forEach((k,v)->System.out.println(k+": "+v));



    }
}
