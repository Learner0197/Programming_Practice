package moviesong;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamTest {
        public static void main(String[] args) {
            List<Integer> list = List.of(44, 87, 56, 44, 93, 54, 33, 12, 10, 1);
            Stream<Integer> stream = list.stream();

            Set<Integer> sqs = stream.map((n) -> n * n).collect(Collectors.toCollection(TreeSet::new));
            System.out.println(sqs);

            stream = list.stream();
            List<Integer> even = stream.filter((n) -> n % 2 == 0).collect(Collectors.toList());
            System.out.println(even);

            stream = list.stream();
            Optional<Integer> total = stream.distinct().reduce((n1, n2) -> n1 + n2);
            if (total.isPresent())
                System.out.println(total.get());

            stream = list.stream();
            System.out.println(stream.distinct().count());

            stream = list.stream();
            Optional<Integer> min = stream.min(Integer::compareTo);
            if (min.isPresent())
                System.out.println(min.get());

            stream = list.stream();
            OptionalDouble ave = stream.mapToDouble(Integer::doubleValue).average();
            if (ave.isPresent())
                System.out.println(ave.getAsDouble());

            stream = list.stream();
            stream.sorted().dropWhile((n) -> n < 20).forEach(System.out::println);

            List<List<Integer>> mylist = List.of(List.of(1, 2, 3),
                    List.of(2, 3, 4),
                    List.of(4, 5, 6),
                    List.of(2, 3, 4));
            mylist.stream().flatMap((l) -> l.stream()).distinct().forEach(System.out::println);
        }
    }
