package day8;

public class DemoThread1 {

    public static void main(String[] args) {

        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0; i<5; i++){
                    System.out.println(Thread.currentThread().getName() + " :" + i);

                    try{
                        Thread.sleep(500);
                    } catch(InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        });
        t1.setName("my thread 1");
        t1.start();

        Runnable r = () -> {
            for(int i=0; i<5; i++){
                System.out.println(Thread.currentThread().getName() + " :" + i);

                try{
                    Thread.sleep(500);
                } catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        };

        Thread t2 = new Thread(r);
        t2.setName("my thread 2");
        t2.start();
        for(int i=0; i<5; i++){
            System.out.println(Thread.currentThread().getName() + " :" + i);
            try{
                Thread.sleep(500);
            } catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
