public class Test{
    public static void main(String[] args){

        Resolution resolution = new Resolution(1920, 1080);
        Monitor monitor = new Monitor("VS197DE","ASUS" ,"18.5", resolution);
        Case computer_case = new Case("Shadow Blade","Shadow","Tempered Glass");
        Motherboard motherboard = new Motherboard("B-250 Pro", "ASUS", 10, "Windows 11");
        Computer computer = new Computer(monitor, motherboard, computer_case);

        computer.getComputerCase().bootUp();
        computer.getMonitor().turn_off_monitor();
        computer.getMotherboard().uploadOS("Ubuntu 16.0");
    }
}
