package Q2;

import java.util.Arrays;
import java.util.Scanner;

public class Student {
	private int rollno;
	private String name;
	int[] marks;
	
	public Student(int rollno, String name, int[] marks) {
		this.rollno = rollno;
		this.name = name;
		this.marks = marks;
	}
	public double calculateAvg() {
		int sum = 0;
		for(int m=0; m<marks.length; m++) {
			sum = sum + marks[m];
		}
		return (double) sum/marks.length;
	}
	
	public double calculatePercent() {
		int sum = 0;
		for(int m=0; m<marks.length; m++) {
			sum = sum + marks[m];
		}
		return (double) (sum/(marks.length * 100.0))*100;
	}

	public void displayDetails() {
		System.out.println("\nStudent:" +name+ "(Rollno:" +rollno+ ")");
		System.out.println("Average Marks:" + calculateAvg());
		System.out.println("Percentage:" + calculatePercent() + "%");
		System.out.println("Student's Marks:" + Arrays.toString(marks));
	}

    @java.lang.Override
    public java.lang.String toString() {
        return "Student{" +
                "rollno=" + rollno +
                ", name='" + name + '\'' +
                ", marks=" + java.util.Arrays.toString(marks) +
                '}';
    }

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println("Enter the marks of the student:");
		int[] marks = new int[n];
		for(int i=0; i<marks.length; i++) {
			marks[i] = sc.nextInt();
		}
		
		Student s1 = new Student(1, "Arnav", marks);
		s1.displayDetails();
	}
}

	
