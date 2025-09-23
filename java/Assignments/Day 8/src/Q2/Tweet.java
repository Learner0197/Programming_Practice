package Q2;

import java.util.Set;

public class Tweet{
    private String subject;
    private int month;
    private int views;
    private Set<String> tags;

    private static int current_month = 9;

    public Tweet(String subject, int month, int views, Set<String> tags) {
        this.subject = subject;
        this.month = month;
        this.views = views;
        this.tags = tags;
    }

    public String getSubject() {
        return subject;
    }

    public int getMonth() {
        return month;
    }

    public int getViews() {
        return views;
    }

    public Set<String> getTags() {
        return tags;
    }

    @Override
    public String toString() {
        return "Tweet{" +
                "subject='" + subject + '\'' +
                ", month=" + month +
                ", views=" + views +
                ", tags=" + tags +
                '}';
    }
}


