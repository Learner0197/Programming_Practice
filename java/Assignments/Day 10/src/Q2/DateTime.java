package Q2;

import java.time.LocalDate;
import java.time.Period;
import java.time.temporal.TemporalAdjuster;
import java.util.function.Predicate;
import java.util.stream.Stream;

public class DateTime {
    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        LocalDate bday = LocalDate.of(2003, 9, 14 );

        Period ageindays = bday.until(today);
        System.out.println("My age is " + ageindays.getYears() + "years, " + ageindays.getMonths() + "months, " + ageindays.getDays() + "days");

        Stream<LocalDate> wholeyear = LocalDate.of(2025, 1, 1).datesUntil(LocalDate.of(2026, 1, 1));
        Predicate<LocalDate> progDay = (d) -> d.getDayOfYear() == 200;
        wholeyear.filter(progDay).forEach(System.out::println);
    }
}
