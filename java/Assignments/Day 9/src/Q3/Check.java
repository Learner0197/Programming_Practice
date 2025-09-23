package Q3;


public class Check {
    public boolean isoddTurn = true;
    public synchronized void eveCheck(int i) {
        while(isoddTurn){
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Even:" + i);
        isoddTurn = true;
        notifyAll();
        }

    public synchronized void oddCheck(int i) {
        while(!isoddTurn){
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Odd:" + i);
        isoddTurn = false;
        notifyAll();
        }
    }


