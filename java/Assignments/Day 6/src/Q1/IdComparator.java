package Q1;

import java.util.Comparator;

public class IdComparator implements Comparator<Toys> {

    @Override
    public int compare(Toys o1, Toys o2) {
        return Integer.compare(o1.getProdid(), o2.getProdid());
    }

}
