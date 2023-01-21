public class Draciel extends Beyblade {
    
    
    private String bitBeast;
    
    public Draciel(String name, int rotationSpeed, int ad, String bitBeast ){
        super(name,rotationSpeed,ad);
        this.bitBeast = bitBeast;
    }


    @Override
    public void bitBeast(){
        System.out.println(getName() + " is unleashing " + bitBeast);
        System.out.println(getName() + "'s defense is the fortress defense!");
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Bit beast name: " + bitBeast);
    }
}
