package Q1;

public class Remote {
	private Curtain curtain;
	
	public Remote(Curtain curtain){
		this.curtain = curtain;
	}
	
	public void pressButton(){
		if(curtain.isOpen()) {
			curtain.Close();
		}
		else {
			curtain.Open();
		}
	}
}
