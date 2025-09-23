package moviesong;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class SongStream {

    public static List<Song> CreateSongList(){
        List<Song> songlist = new ArrayList<>();
        Set<String> singers1 = new TreeSet<>();
        singers1.add("S");
        singers1.add("SH");
        Set<String> singers2 = new TreeSet<>();
        singers2.add("A");
        singers2.add("SU");
        Set<String> singers3 = new TreeSet<>();
        singers3.add("J");
        singers3.add("PH");
        Set<String> singers4 = new TreeSet<>();
        singers4.add("A");
        singers4.add("NA");
        songlist.add(new Song("ssss", 2020, singers1, 5, "mmmm"));
        songlist.add(new Song("aaaa", 2022, singers2, 4, "pppp"));
        songlist.add(new Song("rrrrr", 2020, singers1, 4, "mmmm"));
        songlist.add(new Song("cccc", 2022, singers3, 3, "tttttt"));
        songlist.add(new Song("bbbb", 2022, singers4, 5, "pppppp"));

        return songlist;
    }

    public static void main(String[] args) {
        List<Song> songs = CreateSongList();
        Stream<Song> stream = songs.stream();

        System.out.println("-------Songs by a Singer ----------");
        Predicate<Song> bysinger = (s) -> s.getSingers().contains("S");
        stream.filter(bysinger).forEach(System.out::println);

        System.out.println("----------Map by Movie Title-----------");
        stream=songs.stream();
        Function<Song, Movie> bymovie = (s)-> new Movie(s.getTitle(), s.getMovie());
        stream.map(bymovie).forEach(System.out::println);

        System.out.println("---------------Sort by Title---------------");
        stream=songs.stream();
        stream.sorted(Comparator.comparing(Song::getTitle)).forEach(System.out::println);

        System.out.println("-----------------Sort by Release Year-------------------");
        stream=songs.stream();
        stream.sorted(Comparator.comparing(Song::getReleaseyear)).forEach(System.out::println);

        System.out.println("-----------------Sort by Year and Movie---------------");
        stream=songs.stream();
        Comparator<Song> byyearmovie = Comparator.comparing(Song::getReleaseyear).thenComparing(Comparator.comparing(Song::getMovie));
        stream.sorted(byyearmovie).forEach(System.out::println);

        System.out.println("---------------Group by Movie---------------");
        stream=songs.stream();
        Map<String, List<Song>> moviegrp = stream.collect(Collectors.groupingBy(Song::getMovie));
        moviegrp.forEach((k,v)->System.out.println(k+" "+v));
    }
}

