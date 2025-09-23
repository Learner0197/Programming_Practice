package Q1;

import java.util.Comparator;

public class NameComparator implements Comparator<Toys> {

    @Override
    public int compare(Toys o1, Toys o2) {
        return CharSequence.compare(o1.getName(), o2.getName());
    }

}
