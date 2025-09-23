package moviesong;

public class Movie {
    private String title;
    private String name;

    public Movie(String title, String name) {
        this.title = title;
        this.name = name;
    }

    @Override
    public String toString() {
        return title + "-->" + name ;
    }
}
