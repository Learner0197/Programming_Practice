package Q1;

public class Controller {
	public static void main(String[] args) {
		Curtain curtain = new Curtain();
		Remote remote = new Remote(curtain);
	
	remote.pressButton();
	remote.pressButton();
	remote.pressButton();
}}
