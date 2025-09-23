package day8;

public class DemoThreadMethods {

    public static void main(String[] args){
        Thread t = new Thread(new Thread2());
        t.setName("my thread");
        t.start();
        System.out.println(t.isAlive());

        for(int i=0; i<5; i++){
            System.out.println(Thread.currentThread().getName() + " :" + i);

            if(i==2){
                Thread.yield();
            }

            try{
                Thread.sleep(500);
            } catch(InterruptedException e){
                e.printStackTrace();
            }

        }

        try{
            t.join();
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        System.out.println(t.isAlive());
    }
}
