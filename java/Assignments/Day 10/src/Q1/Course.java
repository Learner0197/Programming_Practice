package Q1;

public enum Course {

    DAI("Diploma in Artificial Intelligence"),
    DAC("DIploma in Advanced Computing"),
    DBDA("Diploma in Big Data Analytics"),
    DVLSI("Diploma in Very Large Scale Integration"),
    DESD("Diploma in Embedded System Design"),
    DUASP("Diploma in Unmanned Aerial Space Program"),
    DITISS("Diploma in Information Technology and Internal Security Systems"),
    DHPCA("Diploma in High Performance Computing and Analysis");

    private String description;

    Course(String description) {
        this.description = description;
    }
}
