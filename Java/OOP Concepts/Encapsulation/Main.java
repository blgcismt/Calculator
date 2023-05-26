public class Main {

    public static void main(String[] args){
        // Subscriber subscriber = new Subscriber();

        // subscriber.name = "Ismet Bilgic";
        // subscriber.balance = 200;
        // subscriber.town = "Tokat";
        
        // subscriber.use(200);

        Improvedsub subscriber = new Improvedsub("Ismet Bilgic", 250, "Tokat");
        subscriber.balanceInquiry();


    }
    
}
