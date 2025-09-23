package day8;

import java.util.Queue;
import java.util.ArrayDeque;

public class MyQueue {

    Queue<String> queue;
    boolean hasvalue;

    public MyQueue() {
        queue = new ArrayDeque<>();
    }

    public synchronized void setValue(String value) {
        if(hasvalue){
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        queue.add(value);
        notifyAll();
        hasvalue = true;
        System.out.println("setValue:"+value);
    }

    public synchronized void getValue() {
        if(!hasvalue){
            try{
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        String value = queue.poll();
        System.out.println("Got Value:"+value);
        notifyAll();
        hasvalue = false;
    }
}
