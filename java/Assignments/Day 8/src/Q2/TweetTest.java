package Q2;

import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TweetTest {

    public static List<Tweet> createTweetList(){
        List<Tweet> tweetList = new ArrayList<>();
        Set<String> tags1 = new HashSet<>();
        Set<String> tags2 = new HashSet<>();
        Set<String> tags3 = new HashSet<>();
        Set<String> tags4 = new HashSet<>();
        tags1.add("#puneweather");
        tags1.add("#rain");
        tags2.add("#food");
        tags2.add("#tasty");
        tags3.add("#travel");
        tags3.add("#mountains");
        tags4.add("#Modi");
        tags4.add("#China");
        tweetList.add(new Tweet("Such a terrible weather",8,123456,tags1));
        tweetList.add(new Tweet("Such a lovely weather",7,45678,tags1));
        tweetList.add(new Tweet("Tasty food in Panchavati",7,12345,tags2));
        tweetList.add(new Tweet("Travelling to Lonavla",9,56789,tags3));
        tweetList.add(new Tweet("Modiji in China",9,1234567,tags4));
        tweetList.add(new Tweet("Such a terrible weather",8,16000,tags1));
        tweetList.add(new Tweet("Tasty food in Panchavati",7,5000,tags2));
        tweetList.add(new Tweet("Modiji in China",9,7000,tags4));


        return tweetList;
    }

    public static void main(String[] args) {
        List<Tweet> tweetList = createTweetList();
        Stream<Tweet> stream = tweetList.stream();

        Predicate<Tweet> thisMonthview = (t) -> t.getMonth() == 9;
        System.out.println("This month's tweets are:");
        stream.filter(thisMonthview).forEach(System.out::println);

        stream = tweetList.stream();
        Predicate<Tweet> viewByHash = (t) -> t.getTags().contains("#puneweather");
        System.out.println("\nviews By Hashtags are:");
        stream.filter(viewByHash).forEach(System.out::println);

        stream = tweetList.stream();
        Predicate<Tweet> subjectCount = (t) -> t.getSubject() == "Modiji in China";
        System.out.println("\nSubject Count is:" + stream.filter(subjectCount).count());

        stream = tweetList.stream();
        Predicate<Tweet> moreViews = (t) -> t.getViews() >= 10000;
        System.out.println("\nTweets with views more than 10000 are:");
        stream.filter(moreViews).forEach(System.out::println);

        stream = tweetList.stream();
        List<Tweet> sortedList = stream.sorted(Comparator.comparingInt(Tweet::getViews).reversed()).limit(5).collect(Collectors.toList());
        System.out.println(("\nTop 5 trending tweets for current month are:"));
        System.out.println(sortedList);
    }
}
