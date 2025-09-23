package day9;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Period;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalAdjuster;
import java.time.temporal.TemporalAdjusters;
import java.util.function.Predicate;
import java.util.stream.Stream;

public class DeoLocalDate {

	public static void main(String[] args) {
		LocalDate today= LocalDate.now();
		System.out.println(today);
		
		LocalDate christmas = LocalDate.of(2025, 12, 25);
		System.out.println(christmas);
		
		System.out.println(christmas.getDayOfMonth());
		System.out.println(christmas.getDayOfWeek());
		System.out.println(christmas.getDayOfYear());
		System.out.println(christmas.getMonth());
		System.out.println(christmas.getMonthValue());
		System.out.println(christmas.getYear());
		
		System.out.println(today.isBefore(christmas));
		
		System.out.println("--------------------");
		LocalDate tomorrow = today.plusDays(1);
		System.out.println(tomorrow);
		LocalDate lastmonth = today.minusMonths(1);
		System.out.println(lastmonth);
		LocalDate future = today.plus(2, ChronoUnit.WEEKS);
		System.out.println(future);
		
		System.out.println("--------------------");
		Period timetochristmas = today.until(christmas);
		System.out.println(timetochristmas);
		System.out.println("Time left for Christmas :" 
				+ timetochristmas.getMonths() + " months "
				+ timetochristmas.getDays() + " days");
		
		System.out.println("--------------------");
		Stream<LocalDate> wholeyear= LocalDate.of(2025, 1, 1).datesUntil(LocalDate.of(2026, 1, 1));
		Predicate<LocalDate> fridays = (d) -> d.getDayOfWeek().equals(DayOfWeek.FRIDAY);
		Predicate<LocalDate> the13th = (d) -> d.getDayOfMonth()==13;
		wholeyear.filter(fridays).filter(the13th).forEach(System.out::println);
		
		System.out.println("--------------------");
		LocalDate secondsun= today.with(TemporalAdjusters.dayOfWeekInMonth(2, DayOfWeek.SUNDAY));
		System.out.println(secondsun);
		
	    LocalDate firstdaynextmonth=today.with(TemporalAdjusters.firstDayOfNextMonth());
	    System.out.println(firstdaynextmonth);
	    
	    LocalDate presat= today.with(TemporalAdjusters.previousOrSame(DayOfWeek.SATURDAY));
	    System.out.println(presat);
	    
	    TemporalAdjuster plustwo = (d) -> d.plus(2, ChronoUnit.DAYS);
	    LocalDate dayafter = today.with(plustwo);
	    System.out.println(dayafter);
	}

	
}
