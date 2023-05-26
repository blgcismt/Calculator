public class Computer {
    
    private Monitor monitor;
    private Motherboard motherboard;
    private Case computer_case;

    public Computer(Monitor monitor, Motherboard motherboard, Case computer_case){
        this.monitor = monitor;
        this.motherboard = motherboard;
        this.computer_case = computer_case;
    }

//write the getter and setters

    public void setMonitor(Monitor monitor){
        this.monitor = monitor;
    }

    public void setMotherboard(Motherboard motherboard){
        this.motherboard = motherboard;
    }

    public void setComputerCase(Case computer_case){
        this.computer_case = computer_case;
    }

    public Monitor getMonitor(){
        return monitor;
    }

    public Motherboard getMotherboard(){
        return motherboard;
    }

    public Case getComputerCase(){
        return computer_case;
    }

}
