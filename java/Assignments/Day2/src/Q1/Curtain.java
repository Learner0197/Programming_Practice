package Q1;

public class Curtain {
	private boolean isOpen;
	
	public Curtain() {
		isOpen = false;
		}
	
	public void Close() {
		if(isOpen) {
			System.out.println("The curtains are closing...");
			isOpen = false;
		}
		else {
			System.out.println("The curtains are closed.");
		}
	}
	
	public void Open() {
		if(!isOpen) {
			System.out.println("The curtains are opening...");
			isOpen = true;
		}
		else {
			System.out.println("The curtains are open.");
			
		}
	}
	
	public boolean isOpen() {
		return isOpen;
		
	}

}

