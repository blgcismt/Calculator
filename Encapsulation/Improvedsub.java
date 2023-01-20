public class Improvedsub {
    
    private String name;
    private int balance = 200;//setting a limit for the balance
    private String town;

    public Improvedsub(String name, int balance, String town){
        this.name = name;
        
        if(balance>0 && balance<=120){
            this.balance = balance;
        }
        this.town = town;
    }

    public void use(int amount){
        if (this.balance - amount < 0){
            System.out.println("Balance not high enough!");
        }

        else{
            this.balance -= amount;

            if(this.balance == 0){
                System.out.println("Your balance is 0. Please visit one of our centers to replenish your credit.");
            }

            else{
                System.out.println("New balance: " + balance);
            }
        }
    
    }

    public void balanceInquiry(){
        System.out.println("Your balance: " + balance);
    }
}
