package day9;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Set;

public class DemoZones {

	public static void main(String[] args) {
		
		LocalDateTime dt = LocalDateTime.now();
		System.out.println(dt);
		
		Set<String> zones= ZoneId.getAvailableZoneIds();
		System.out.println(zones);
		
		ZonedDateTime ist = dt.atZone(ZoneId.of("Asia/Kolkata"));
		System.out.println(ist);
		
		//zone info added to Indian time as per system dt
		ZonedDateTime london = dt.atZone(ZoneId.of("Europe/London"));
		System.out.println(london);
		
		//Actual time in London
		london =ist.toInstant().atZone(ZoneId.of("Europe/London"));
		System.out.println(london);
		
		LocalDateTime istloc = ist.toLocalDateTime();
		LocalDateTime londonlocal = london.toLocalDateTime();
		
		System.out.println(istloc);
		System.out.println(londonlocal);
		
		System.out.println(Duration.between(istloc, londonlocal));

	}

}
