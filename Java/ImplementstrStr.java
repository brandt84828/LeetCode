public class ImplementstrStr {
    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "ll";
        /*
        if(haystack == null || needle == null)
            return -1;
        else if(needle.equals(""))
            return 0;
        else if(haystack.length() == needle.length()) {
            return haystack.equals(needle) ? 0 : -1;
        }

        //重要(要記得扣needle長度，不然後續問題多)
        for(int i = 0; i < haystack.length() - needle.length() + 1; i++) {  //這邊先扣needle長度避免haystack從最後幾位開始往後取超過界限以及needle>haystack直接不進入迴圈回傳-1
            if(haystack.charAt(i) == needle.charAt(0)
               && haystack.substring(i, i+needle.length()).equals(needle))
                return i;
        }
        return -1;
         */



    }
}
