import java.util.ArrayList;

public class HappyNumber {

    public static void main(String[] args) {

    int n = 38;
    System.out.print(HappyNumber.isHappy(n));


    }

    public static boolean isHappy(int n) {
        ArrayList<Integer> a = new ArrayList<>();
        int x = n ;
        int re;
        int total = 0;
        while(a.contains(n)==false){
            a.add(n);
            for(int i = 1;i<=Integer.toString(n).length();i++){
                 re =  x % 10;
                 x = x / 10;
                 total = total + re * re;

            }
            n = total ;
            System.out.println(n);
            x = n ;
            total = 0;
        }

        if(n==1){
            return true;
        }
        else{
            return false;
        }


    }
}
