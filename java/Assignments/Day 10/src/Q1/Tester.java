package Q1;
import Q1.Course;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Tester {
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        StudentTest s = new StudentTest();
        Student s1 = new Student("A1", "Arnav", 23, "DAI", LocalDate.of(2025, 8, 1), 7.8, "Dombiwali");
        Student s2 = new Student("A2", "Aman", 24, "DHPCA", LocalDate.of(2024, 8, 1), 7.9, "Kanpur");
        Student s3 = new Student("A3", "Arunesh", 25, "DAI", LocalDate.of(2023, 8, 1), 8.0, "Delhi");
        Student s4 = new Student("A4", "Atharv", 26, "DBDA", LocalDate.of(2022, 8, 1), 8.1, "Pune");
        Student s5 = new Student("A5", "John", 27, "DAC", LocalDate.of(2021, 8, 1), 8.2, "xyz");

        students.add(s1);
        students.add(s2);
        students.add(s3);
        students.add(s4);
        students.add(s5);
        System.out.println("Available Courses");
        for(Course c : Course.values()) {
            System.out.println(c.name());
        }
        System.out.println(s.getStudentNamesByCourse(students,"DAI"));
        System.out.println(s.getStudentNamesByCourse(students,"DBDA"));
        System.out.println(s.getStudentNamesByCourse(students,"Pune"));
    }
}
