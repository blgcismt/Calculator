public class Employee{
    private String name;
    private String surname;
    private int id;


    public Employee(){
        this.name = "No name";
        this.surname = "No surname";
        this.id = 0;
    }

    public Employee( String name, String surname, int id){
        this.name = name;
        this.surname = surname;
        this.id = id;
    }

    public void showInfo(){
        System.out.println("Here are the information on the employe:");
        System.out.println("Employee name: " + name);
        System.out.println("Employee surname: " + surname);
        System.out.println("Employee id: " + id);
    }

    public String getName(){
        return name;
    }

    public String getSurname(){
        return surname;
    }

    public int getId(){
        return id;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setSurname(String surname){
        this.surname = surname;
    }

    public void setId(int id){
        this.id = id;
    }


}
