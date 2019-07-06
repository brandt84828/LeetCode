import java.util.ArrayList;

public class SelfDividingNumbers {
     public static void main(String[] args) {

         int left = 1;
         int right = 22;

        //Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

         boolean ans  = true;
         ArrayList A = new ArrayList();
         int mod;
         int cal;
         for(int i = left;i<=right;i++){
             cal = i;
             for(int j = 0;j<String.valueOf(i).length();j++){
                 mod = cal % 10;
                 cal = cal / 10;
                 if(mod == 0){
                    ans = false;
                 }else if(i % mod != 0){
                     ans = false;
                 }
             }

             if(ans==true){
                 A.add(i);
             }
             ans = true;
         }


         System.out.print(A);




    }
}
