public class Driger extends Beyblade {
    
    
    private String bitBeast;
    
    public Driger(String name, int rotationSpeed, int ad, String bitBeast ){
        super(name,rotationSpeed,ad);
        this.bitBeast = bitBeast;
    }


    @Override
    public void bitBeast(){
        System.out.println(getName() + " is unleashing " + bitBeast);
        System.out.println(getName() + "'s attack is the tiger claw!");
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Bit beast name: " + bitBeast);
    }
}
