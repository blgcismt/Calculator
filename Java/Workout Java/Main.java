import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the workout program!");

        String moves = "Available moves\n"
                       +"1 - Burpees\n" 
                       +"2 - Push ups\n"
                       +"3 - Sit ups\n "
                       +"4 - Squats";
         
        System.out.println(moves);

        System.out.println("Build your workout...");

        System.out.print("Enter the amount of burpess you would like to perform: ");
        int burpeeCount = scanner.nextInt();

        System.out.print("Enter the amount of push ups you would like to perform: ");
        int pushupCount = scanner.nextInt();

        System.out.print("Enter the amount of sit ups you would like to perform: ");
        int situpCount = scanner.nextInt();

        System.out.print("Enter the amount of squats you would like to perform: ");
        int squatCount = scanner.nextInt();
        scanner.nextLine();


        Workout workout = new Workout(burpeeCount, pushupCount, situpCount, squatCount);

        System.out.print("Workout starting....");

        while (workout.endWorkout() == false){

            System.out.print("Which move would you like to perform? (Burpee,Pushup,Squat,Situp): ");
            String move = scanner.nextLine();

            System.out.print("How many of this move would you like to perform: ");
            int number = scanner.nextInt();
            scanner.nextLine();

            workout.performMove(move, number);

        }

        System.out.println("Workout session completed successfully...");


    }
}
