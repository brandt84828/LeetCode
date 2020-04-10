public class LongestCommonPrefix {
    public static void main(String[] args) {
        String strs[] = {"flower","flow","flight"};
        /*
        if(strs==null||strs.length==0) return "";

        for(int i=0;i<strs[0].length();i++){
            char now = strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                if(i==strs[j].length() || strs[j].charAt(i)!=now){
                    return strs[0].substring(0, i); //這邊不用return的話，charAt會超出index
                }
            }
        }

        return strs[0];

        */
    }
}
