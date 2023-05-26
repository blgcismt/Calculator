public class Account{

    private String username;
    private String password;
    private double balance;

    double amountWithdrawn = 0;

    public Account(String username, String password, double balance){
        this.username = username;
        this.password = password;
        this.balance = balance;
    }

    public String getUsername(){
        return username;
    }

    public void setUsername(String username){
        this.username = username;
    }

    public String getPassword(){
        return password;
    }

    public void setPassword(String password){
        this.password = password;
    }

    public double getBalance(){
        return balance;
    }

    public void setBalance(double balance){
        this.balance = balance;
    }

    public void depositMoney(double amount){
        balance += amount;
        System.out.println("New balance: " + balance + " $");
    }

    public void withdrawMoney(double amount){
        if ((amount > 1000) || (amountWithdrawn == 1000) ){
            System.out.println("Your demand is over the daily limit. You cannot withddraw more than 1000$ in a day.");
        }

        else if ((balance - amount) < 0){
            System.out.println("Your balance is not enough. Your balance: " + balance + " $");
        }

        else{
            amountWithdrawn += amount;
            balance -= amount;
            System.out.println("New balance: " + balance + " $");
        }
    }


}
