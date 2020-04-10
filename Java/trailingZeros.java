public class trailingZeros {
    public static void main(String[] args) {
        int n = 0;//此n為己階層(leetocde input)
        int count = 0;
        while (n > 0) {
            n = n / 5;
            count = count + n;
        }

        System.out.print(count);
    }
}
