public class Monitor {
    
    private String model;
    private String producer;
    private String size;
    private Resolution resolution;

    public Monitor(String model, String producer, String size, Resolution resolution){
        this.model = model;
        this.producer = producer;
        this.size = size;
        this.resolution = resolution;
    }

    public void turn_off_monitor(){
        System.out.println("Monitor is being turned off...");
    }

    public void setModel(String model){
        this.model = model;
    }

    public void setProducer(String producer){
        this.producer = producer;
    }

    public void setSize(String size){
        this.size = size;
    }

    public void setResolution(Resolution resolution){
        this.resolution = resolution;
    }

    public String getModel(){
        return model;
    }

    public String getProducer(){
        return producer;
    }

    public String getSize(){
        return size;
    }

    public Resolution getResolution(){
        return resolution;
    }






}
