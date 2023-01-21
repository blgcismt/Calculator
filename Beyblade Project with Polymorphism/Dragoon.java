public class Dragoon extends Beyblade {
    
    
    private String bitBeast;
    private String specialAbility;
    
    public Dragoon(String name, int rotationSpeed, int ad, String bitBeast, String specialAbility ){
        super(name,rotationSpeed,ad);
        this.bitBeast = bitBeast;
        this.specialAbility = specialAbility;
    }


    @Override
    public void bitBeast(){
        System.out.println(getName() + " is unleashing " + bitBeast);
        System.out.println(getName() + "'s attack is the phantom hurricane!");
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Bit beast name: " + bitBeast);
        System.out.println("Special ability: " + specialAbility);
    }
}
