package Q1;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
public class Numbers {
    public static boolean operateOnNumber(Predicate<Integer> p,int n){
        return p.test(n);
    }
    public static void operateOnNumbers(Predicate p, List<Integer> numbers){
        List<Integer> result = new ArrayList<>();
        for(Integer i : numbers){
            if(p.test(i)){
                System.out.println(i);
            }
        }
    }
}
