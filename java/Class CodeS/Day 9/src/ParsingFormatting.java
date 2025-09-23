package day9;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ParsingFormatting {

	public static void main(String[] args) {
		String mydate = "20-10-2025 10:45";
		
		//String to date
		LocalDateTime dt=LocalDateTime.parse(mydate, 
				DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm"));
		System.out.println(dt);
		
		//date to String
		mydate = dt.format(DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm"));
		System.out.println(mydate);
		
		mydate = dt.format(DateTimeFormatter.ofPattern("E-MM-yy HH:mm a"));
		System.out.println(mydate);
		
		

	}

}
