public class Beyblade {

    

    private String name;
    private int rotationSpeed;
    private int ad;


    public Beyblade(String name, int rotationSpeed, int ad){
        this.name = name;
        this.rotationSpeed = rotationSpeed;
        this.ad = ad;
    }


    public String getName(){
        return name;
    }

    public int getRotationSpeed(){
        return rotationSpeed;
    }

    public int getAD(){
        return ad;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setRotationSpeed(int rotationSpeed){
        this.rotationSpeed = rotationSpeed;
    }

    public void setAD(int ad){
        this.ad = ad;
    }


    public void attack(){
        System.out.println(name + " is attacking with an attack damage of " + ad + " and " + " a rotation speed of " + rotationSpeed);

    }

    public void bitBeast(){
        System.out.println("This beyblade does not have a bit beast...");
    }

    public void showInfo(){
        System.out.println("Name of the beyblader: " + name);
        System.out.println("Attack damage of the beyblader: " + ad);
        System.out.println("Rotation speed of the beyblader: " + rotationSpeed);
    }

}
