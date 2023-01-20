import java.util.Scanner;

public class Atm {

    public void boot(Account account){
        Login login = new Login();

        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the ATM!");
        System.out.println();
        System.out.println();

        System.out.println("User Login");
        System.out.println("===============");

        int attempt = 3;

        while (true) {

            if(login.login(account)){
                System.out.println("Attempt successful");
                break;

            }

            else{
                System.out.println("Attempt unsuccessful...");
                attempt -= 1;
                System.out.println("Remaining attempts: " + attempt);
            }

            if (attempt == 0){
                System.out.println("You have run out of attempts...");
                return;
            }

            
        }

        System.out.println("===============");

        String actions = "1 - Balance inquiry\n"
                          + "2 - Deposit \n"
                          + "3 - Withdrawal \n"
                          + "4 - Press 'x' to exit";

        System.out.println(actions);

        System.out.println("===============");


        while (true){
            System.out.print("Choose your action: ");
            String action = scanner.nextLine();

            if (action.equals("x")){
                System.out.println("Goodbye...");
                break;
            }

            else if (action.equals("1")){
                System.out.println("Your balance: " + account.getBalance());
            }

            else if (action.equals("2")){
                System.out.print("Please enter the amount you would like to deposit: ");
                int amount = scanner.nextInt();
                scanner.nextLine();
                account.depositMoney(amount);
            }

            else if (action.equals("3")){
                System.out.print("Enter the amount you would like to withdraw: ");
                int amount = scanner.nextInt();
                scanner.nextLine();
                account.withdrawMoney(amount);
            }

            else{
                System.out.println("Invalid action... Please check your input!");
            }


        }

        
    }
    
}
