import java.util.ArrayList;

public class SortArrayByParity {
    public static void main(String[] args) {

        int[] A = {0,1};
        int start = 0;
        int end = A.length - 1; //array 從0開始
        int temp;
        for(int i = 0;i<A.length;i++){
            if(start<end){
                if (A[start] % 2 == 1 && A[end] % 2 == 0){
                    temp = A[start];
                    A[start] = A[end];
                    A[end] = temp;
                }
                else if(A[start] % 2 == 0 && A[end] % 2 == 1){
                    start++;
                    end--;
                }
                else if(A[start] % 2 == 0 ){
                    start++;
                }
                else {
                    end--;
                }
            }

        }

        for(int x:A)
        System.out.print(x);
    }


}
