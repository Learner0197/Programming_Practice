package day9;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class DemoLocalTime {

	public static void main(String[] args) {
		LocalTime now = LocalTime.now();
		System.out.println(now);		
		LocalTime noon= LocalTime.NOON;		
		System.out.println(now.isBefore(noon));
		
		Duration diff= Duration.between(now, noon);
		System.out.println(diff);
		System.out.println(diff.toHoursPart() + " hrs "
		+ diff.toMinutesPart() + " mins");
		
		System.out.println("------------------------------");
		LocalDateTime current = LocalDateTime.now();
		System.out.println(current);
		
		current = LocalDateTime.of(2025, 9, 4, 9, 38, 30);
		System.out.println(current);
		
		LocalDateTime today = LocalDateTime.of(LocalDate.now(), LocalTime.now());
		System.out.println(today);
		
		LocalDateTime dt= LocalDate.of(2025, 9, 10).atTime(LocalTime.of(12, 30));
		System.out.println(dt);
	}
}
