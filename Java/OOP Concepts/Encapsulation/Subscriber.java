public class Subscriber{

    public String name;
    public int balance;
    public String town;

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
