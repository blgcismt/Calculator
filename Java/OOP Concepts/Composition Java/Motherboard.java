public class Motherboard {

    private String model;
    private String producer;
    private int socket_count;
    private String OS;


    public Motherboard(String model, String producer, int socket_count, String OS){
        this.model = model;
        this.producer = producer;
        this.socket_count = socket_count;
        this.OS = OS;
    }

    public void uploadOS(String OS){
        this.OS = OS;

        System.out.println("The OS has been successfully uploaded...");
        System.out.println("Your new OS is: " + OS);
    }

    public void setModel(String model){
        this.model = model;
    }

    public void setProducer(String producer){
        this.producer = producer;
    }

    public void setSocketCount(int socket_count){
        this.socket_count = socket_count;
    }

    public void setOS(String OS){
        this.OS = OS;
    }

    public String getModel(){
        return model;
    }

    public String getProducer(){
        return producer;
    }

    public int getSocketCount(){
        return socket_count;
    }

    public String getOS(){
        return OS;
    }



}
