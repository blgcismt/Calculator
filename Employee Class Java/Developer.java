public class Developer extends Employee{
    
    private String languages;
    


    public Developer(String name,String surname,int id, String languages){
        super(name,surname,id);
        this.languages = languages;
    }

    public void uploadOS(String os){
        System.out.println(getName() + " " + getSurname() + " is uploading an OS.");
    }

    @Override
    public void showInfo(){
        super.showInfo();
        System.out.println("Languages that are known by the developer: " + languages);
    }

    public String getLanguages(){
        return languages;
    }

    public void setLanguages(String languages){
        this.languages = languages;
    }

    


}
