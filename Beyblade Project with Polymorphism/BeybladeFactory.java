public class BeybladeFactory {  

    public Beyblade produceBeyblade(String beybladeType){

        if (beybladeType.equals("Dragoon")){
            return new Dragoon("Takao",1000,500,"Blue Wind Dragon of the East","Talk with a bit beast");
        }

        else if (beybladeType.equals("Dranzer")){
            return new Dranzer("Kai",800,600,"Sacred Red Phoenix");
        }

        else if (beybladeType.equals("Driger")){
            return new Driger("Rei",1000,450,"White Tiger of the West");
        }

        else if (beybladeType.equals("Draciel")){
            return new Draciel("Max",600,1200,"Water Turtle");
        }

        else{
            return null;
        }
    }
    
}
