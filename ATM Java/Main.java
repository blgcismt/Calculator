public class Main {

    public static void main(String[] args){

        Atm atm = new Atm();

        Account account = new Account("John Doe","12345",2000.0);


        atm.boot(account);
        System.out.println("Exitting... Goodbye!");
    }
    
}
