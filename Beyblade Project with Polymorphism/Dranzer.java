public class Dranzer extends Beyblade {

    private String bitBeast;
    
    public Dranzer(String name, int rotationSpeed, int ad, String bitBeast ){
        super(name,rotationSpeed,ad);
        this.bitBeast = bitBeast;
    }


    @Override
    public void bitBeast(){
        System.out.println(getName() + " is unleashing " + bitBeast);
        System.out.println(getName() + "'s attack is the flame saber!");
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Bit beast name: " + bitBeast);
    }

}
