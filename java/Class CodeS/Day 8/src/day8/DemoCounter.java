package day8;

public class DemoCounter {

    public static void main(String[] args){
        Counter c = new  Counter();
        new Thread(new Runnable(){
            @Override
            public void run(){
                synchronized (c){
                    for(int i=0; i<50; i++){
                        c.increment();
                        System.out.println("Count: " + c.getCount());

                        try{
                            Thread.sleep(500);
                        } catch(InterruptedException e){
                            e.printStackTrace();
                        }
                    }
                }
            }
        }).start();

        new Thread(new Runnable(){
            @Override
            public void run(){
                synchronized (c){
                    for(int i=0; i<50; i++){
                        c.increment();
                        System.out.println("Count: " + c.getCount());

                        try{
                            Thread.sleep(500);
                        } catch(InterruptedException e){
                            e.printStackTrace();
                        }
                    }
                }
            }
        }).start();

        CounterJob job = new  CounterJob();
        Thread t1 = new Thread(job);
        Thread t2 = new Thread(job);

        t1.start();
        t2.start();
    }
}
