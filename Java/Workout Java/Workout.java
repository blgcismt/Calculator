public class Workout {

    private int burpeeCount;
    private int pushupCount;
    private int situpCount;
    private int squatCount;


    public Workout(int burpeeCount, int pushupCount, int situpCount, int squatCount) {
        this.burpeeCount = burpeeCount;
        this.pushupCount = pushupCount;
        this.situpCount = situpCount;
        this.squatCount = squatCount;
    }

    public int getBurpeeCount() {
        return burpeeCount;
    }

    public void setBurpeeCount(int burpeeCount) {
        this.burpeeCount = burpeeCount;
    }

    public int getPushupCount() {
        return pushupCount;
    }

    public void setPushupCount(int pushupCount) {
        this.pushupCount = pushupCount;
    }

    public int getSitupCount() {
        return situpCount;
    }

    public void setSitupCount(int situpCount) {
        this.situpCount = situpCount;
    }

    public int getSquatCount() {
        return squatCount;
    }

    public void setSquatCount(int squatCount) {
        this.squatCount = squatCount;
    }

    public void doBurpee(int numberofMoves){
        if (burpeeCount == 0){
            System.out.println("You have done all the required burpees for today!");
        }

        if (burpeeCount - numberofMoves <0){
            System.out.println("You've outdone your target for the day. Congratulations!");
            burpeeCount = 0;
            System.out.println("Remaining burpees for the day: " + burpeeCount);
        }

        else {
            burpeeCount -= numberofMoves;
            System.out.println("Remaining burpees for the day: " + burpeeCount);
        }

     }   


    
        public void doPushUp(int numberofMoves){
            if (pushupCount == 0){
                System.out.println("You have done all the required push ups for today!");
            }
    
            if (pushupCount - numberofMoves <0){
                System.out.println("You've outdone your target for the day. Congratulations!");
                pushupCount = 0;
                System.out.println("Remaining push ups for the day: " + pushupCount);
            }
    
            else {
                pushupCount -= numberofMoves;
                System.out.println("Remaining pushup for the day: " + pushupCount);
            }

        }

        public void doSitUp(int numberofMoves){
            if (situpCount == 0){
                System.out.println("You have done all the required sit ups for today!");
            }
    
            if (situpCount - numberofMoves <0){
                System.out.println("You've outdone your target for the day. Congratulations!");
                situpCount = 0;
                System.out.println("Remaining sit ups for the day: " + situpCount);
            }
    
            else {
                situpCount -= numberofMoves;
                System.out.println("Remaining sit ups for the day: " + situpCount);
            }

        }

        public void doSquat(int numberofMoves){

            if (squatCount == 0){
                System.out.println("You have done all the required squats for today!");
            }
    
            if (squatCount - numberofMoves <0){
                System.out.println("You've outdone your target for the day. Congratulations!");
                squatCount = 0;
                System.out.println("Remaining squats for the day: " + squatCount);
            }
    
            else {
                squatCount -= numberofMoves;
                System.out.println("Remaining squats for the day: " + squatCount);
            }

    }

    public void performMove(String move, int numberofMoves){
        if(move.equals("Burpee")){
            doBurpee(numberofMoves);
        }

        else if (move.equals("Pushup")){
            doPushUp(numberofMoves);
        }

        else if (move.equals("Situp")){
            doSitUp(numberofMoves);
        }

        else if (move.equals("Squat")){
            doSquat(numberofMoves);
        }

        else{
            System.out.println("Please choose an existing move!");
        }
    }


    public boolean endWorkout(){
        if (burpeeCount == 0 && pushupCount == 0 && situpCount == 0 && squatCount == 0){
            return true;
        }

        else{
            return false;
        }

    }
    
}
