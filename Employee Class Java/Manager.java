public class Manager extends Employee{
    private int underlings;


    public Manager(String name,String surname,int id,int underlings){
        super(name,surname,id);
        this.underlings = underlings;
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Number of people for whom the manager is responsible: " + underlings );
    }

    public void giveRaise(int amount){
        System.out.println(getName() + " " + getSurname() + " is giving a raise of " + amount + "$.");
    }

    public int getUnderlings(){
        return underlings;
    }

    public void setUnderlings(int underlings){
        this.underlings = underlings;
    }


}
