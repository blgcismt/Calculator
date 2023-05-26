import java.util.Scanner;


public class Main {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the employee portal!");

        String actions = "Here are the actions you can take:\n"
                        +"1 - Access the developer class\n"
                        + "2 - Access the manager class\n"
                        + "3 - Press 'x' to exit.";
        
        System.out.println(actions);

        while (true){

            System.out.print("Choose your action: ");
            String action = scanner.nextLine();

            if (action.equals("x")){
                System.out.println("Exitting the portal... Goodbye!");
                break;
            }

            else if (action.equals("1")){
                Developer developer = new Developer("Ismet","Bilgic",122,"Python,Java,C++");
                System.out.println("Developer actions:");
                String developer_action = "1 - Upload an OS\n"
                                        + "2 - Show information\n"
                                        + "3 - Press 'x' to exit.";

                System.out.println(developer_action);
                while (true){
                    System.out.print("Choose your action: ");
                    String d_action = scanner.nextLine();

                    if (d_action.equals("x")){
                        System.out.println("Exitting the developer portal...");
                        break;
                    }


                    else if (d_action.equals("1")){
                        System.out.print("Enter the OS: ");
                        String os = scanner.nextLine();
                        developer.uploadOS(os);
                    }

                    else if (d_action.equals("2")){
                        developer.showInfo();
                    }

                    else{
                        System.out.println("Invalid action, please check your input!");
                    }
                }
            }

            else if(action.equals("2")){
                Manager manager = new Manager("Berkay","Caliskan",123,10);
                System.out.println("Manager actions:");
                String manager_action = "1 - Give a raise\n"
                                        + "2 - Show information\n"
                                        + "3 - Press 'x' to exit.";

                System.out.println(manager_action);

                while (true){
                    System.out.print("Choose your action: ");
                    String m_action = scanner.nextLine();

                    if (m_action.equals("x")){
                        System.out.println("Exitting the manager portal...");
                        break;
                    }

                    else if (m_action.equals("1")){
                        System.out.print("How much raise would you like to give: ");
                        int amount = scanner.nextInt();
                        scanner.nextLine();
                        manager.giveRaise(amount);
                    }

                    else if (m_action.equals("2")){
                        manager.showInfo();
                    }

                    else{
                        System.out.println("Invalid action, please check your input!");
                    }
                }
            }

            else{
                System.out.println("Invalid action, please check your input!");
            }

        
        }
    }
}
