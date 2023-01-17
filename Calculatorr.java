import java.util.Scanner;


public class Calculatorr {

    public static int subtraction(int a,int b) {
        
        return (a - b);
        
    }
    public static double division(int a,int b) {
        return ((double)a / b);
        
    }
    public static int addition(int a,int b){
        
        return (a + b);
        
    }
    public static int addition(int a,int b,int c) {
        
        return (a + b + c);
    }
    public static int multiplication(int a,int b) {
        
        return a * b;
    }
    public static int multiplication(int a,int b,int c) {
        return a * b * c;
        
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String actions =  "1. Addition\n"
                           +"2. Subtraction\n"
                           + "3. Multiplication\n"
                           + "4. Division\n"
                           + "Press q to exit.";
        System.out.println("****************************************");
        System.out.println(actions);
        System.out.println("****************************************");

        while (true) {
            System.out.print("Choose your action : ");
            String act = scanner.nextLine();
            
            if (act.equals("q")){
                
                System.out.println("Exitting the calculator goodbye...");
                break;
            }
            else if (act.equals("1")) {
                System.out.print("How many values will you be using? (2 or 3): ");
                
                int hm = scanner.nextInt();
                
                if (hm == 2) {
                    System.out.print("a:");
                    int a = scanner.nextInt();
                    System.out.print("b:");
                    int b = scanner.nextInt();
                    scanner.nextLine();
                    
                    System.out.println("Sum of the given numbers : " + (addition(a, b)));
                    
                    
                }
                else if (hm == 3) {
                    System.out.print("a:");
                    int a = scanner.nextInt();
                    System.out.print("b:");
                    int b = scanner.nextInt();
                    System.out.print("c:");
                    int c = scanner.nextInt();
                    scanner.nextLine();
                    
                    System.out.println("Sum of the given numbers : " + (addition(a, b,c)));
                    
                }
                else {
                    
                    System.out.println("No such method exists...");
                }
                
                
            }
            else if (act.equals("2")) {
                System.out.print("a:");
                int a = scanner.nextInt();
                System.out.print("b:");
                int b = scanner.nextInt();
                scanner.nextLine();
                
                System.out.println("The difference of the given numbers : " + subtraction(a, b));
                
            }
            else if (act.equals("3")){
                System.out.print("How many values will you be using ? (2 veya 3): ");
                
                int hm = scanner.nextInt();
                
                if (hm == 2) {
                    System.out.print("a:");
                    int a = scanner.nextInt();
                    System.out.print("b:");
                    int b = scanner.nextInt();
                    scanner.nextLine();
                    
                    System.out.println("The product of the given numbers is: " + (multiplication(a, b)));
                    
                    
                }
                else if (hm == 3) {
                    System.out.print("a:");
                    int a = scanner.nextInt();
                    System.out.print("b:");
                    int b = scanner.nextInt();
                    System.out.print("c:");
                    int c = scanner.nextInt();
                    scanner.nextLine();
                    
                    System.out.println("The product of the given numbers is : " + (multiplication(a, b,c)));
                    
                }
                else {
                    
                    System.out.println("No such method exists...");
                }
                
            }
            else if (act.equals("4")) {
                System.out.print("a:");
                int a = scanner.nextInt();
                System.out.print("b:");
                int b = scanner.nextInt();
                scanner.nextLine();
                
                System.out.println("The result is : " + division(a, b));
                
            }
            else {
                System.out.println("Invalid action...");
            }
            
            
            
        }
        
        
    }
}