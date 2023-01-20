public class Case {
    
    private String model;
    private String producer;
    private String material;

    public Case(String model, String producer, String material){
        this.model = model;
        this.producer = producer;
        this.material = material;
    }

    public void bootUp(){
        System.out.println("Computer booting up...");
    }

    public void setModel(String model){
        this.model = model;
    }

    public void setProducer(String producer){
        this.producer = producer;
    }

    public void setMaterial(String material){
        this.material = material;
    }

    public String getModel(){
        return model;
    }

    public String getProducer(){
        return producer;
    }

    public String getMaterial(){
        return material;
    }



}
