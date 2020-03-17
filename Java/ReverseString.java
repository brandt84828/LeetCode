public class ReverseString {
    public static void main(String[] args) {
        // write your code here
        char[] a = {'h','e','l','l','o'};

        int left = 0;
        int right = a.length - 1;

        while(left<right){
            char temp = a[left];
            a[left] = a[right];
            a[right] = temp;
            left++;
            right--;
        }

        System.out.println(a);

    }
}
