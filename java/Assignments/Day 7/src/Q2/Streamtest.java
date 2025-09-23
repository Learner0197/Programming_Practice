package Q2;
import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.ArrayList;
import java.util.Comparator;



public class Streamtest {
    public static void main(String[] args) {
        String [] arr = {"Mango", "orange", "Grapes", "apple", "Banana", "strawberry", "Watermelon"};
        Stream<String> fruits = Arrays.stream(arr);
        Stream<String> fru = fruits;

        List<String> fruit = fruits.collect(Collectors.toList());
        System.out.println(fruit);

        List<String> upper = fruit.stream().map(String::toUpperCase).collect(Collectors.toList());
        System.out.println(upper);

        List<String> lower = fruit.stream().map(String::toLowerCase).collect(Collectors.toList());
        System.out.println(lower);

        System.out.println(fruit.stream().filter(f->f.toLowerCase().compareTo("n")<0).sorted().collect(Collectors.toList()));

        System.out.println(fruit.stream().filter(f->f.toLowerCase().compareTo("n")<0).sorted(Collections.reverseOrder()).collect(Collectors.toList()));

        System.out.println(fruit.stream().filter(f->f.compareTo("[")<0).sorted().collect(Collectors.toList()));
        List<String> fr =fruit.stream().filter(f->f.toLowerCase().compareTo("z")<=0).sorted().toList();

        System.out.println(fr.stream().filter(f->f.toLowerCase().length()<=6).sorted(Collections.reverseOrder()).collect(Collectors.toList()));

        System.out.println(fruit.stream().sorted(Comparator.comparingInt(String::length)).collect(Collectors.toList()));
    }
}
