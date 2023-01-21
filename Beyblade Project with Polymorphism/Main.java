import java.util.Scanner;

public class Main{

    public static void main(String[] args){

        System.out.println("Welcome to the Beyblade Progam!");
        System.out.println("Press 'x' to exit...");

        Scanner scanner = new Scanner(System.in);

        while (true){
            System.out.println("Which beyblade would you like to produce?");
            String move = scanner.nextLine();

            if (move.equals("x")){
                System.out.println("Goodbye!");
                break;
            }

            else{
                BeybladeFactory factory = new BeybladeFactory();
                Beyblade beyblade =  factory.produceBeyblade(move);

                if (beyblade == null){
                    System.out.println("Please enter a valid beybalde name!");
                }

                else{
                    beyblade.showInfo();
                    beyblade.attack();
                    beyblade.bitBeast();
                }

            }


        }
        
    }
}
