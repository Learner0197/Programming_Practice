package Q1;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class StudentTest {

    public List<String> getStudentNamesByCourse(List<Student> students,  String course) {
        return students.stream().filter((s)-> s.getCourse().equals(course)).map(Student::getName).toList();
    }

    public List<Student> getStudentGPA(List<Student> students,  double mingpa) {
        return students.stream().filter((s)-> s.getGpa()>=mingpa).toList();
    }

    public Set<String> getAllCities(List<Student> students) {
        return students.stream().map(Student::getCity).collect(Collectors.toSet());
    }

    public Map<String, Long> getStudentCountByCourse(List<Student> students) {
        return students.stream().collect(Collectors.groupingBy(Student::getCourse, Collectors.counting()));
    }

    public double getAverageGPA(List<Student> students) {
        return students.stream().collect(Collectors.averagingDouble(Student::getGpa));
    }

    public List<Student> getTopStudentsByGPA(List<Student> students, int limit) {
        return students.stream().sorted(Comparator.comparingDouble(Student::getGpa).reversed()).limit(limit).collect(Collectors.toList());
    }





}
