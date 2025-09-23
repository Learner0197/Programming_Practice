package Q1;

import Q1.Numbers;

import java.util.List;
import java.util.function.Predicate;

import static Q1.Numbers.operateOnNumbers;

public class Test {
    public static void main(String[] args) {
        Predicate<Integer> check = (n) -> n>0;
        System.out.println(check.test(-10));

        Predicate<Integer> check2 = (n) -> {
            int count = 0;
            for(int i =1; i<=n; i++){
                if(n%i==0){
                    count++;
                }
            }
            if(count>2){
                return false;
            }
            else{
                return true;
            }
        };
        System.out.println(check2.test(11));
//        if(Numbers.operateOnNumber(check2,17)){
//            System.out.println("The given number is not Prime Number");
//        }
//        else {
//            System.out.println("The given number is Prime Number");
//        }

        List<Integer> numbers = List.of(10,12,13,31,33,29,23,30,60,120);
        Predicate<Integer> even = i -> i%2==0;
        Predicate<Integer> Div_2_3_5 = i -> i%2==0 && i%3==0 && i%5==0;

        Numbers.operateOnNumbers(even, numbers);
        Numbers.operateOnNumbers(Div_2_3_5, numbers);
        }
    }
