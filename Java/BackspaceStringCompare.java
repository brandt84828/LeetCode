public class BackspaceStringCompare {
    public static void main(String[] args) {
        // space complexity not O(1)
        String  S = "a##c", T = "#a#c";
        String S_RES="",T_RES = "";

        for(int i=0;i<S.length();i++){
            if(S.charAt(i)!=35){
                S_RES = S_RES + S.charAt(i);
            }
            if(S.charAt(i)==35 && !S_RES.equals("")){
                S_RES = S_RES.substring(0,S_RES.length() - 1);
            }
        }

        for(int i=0;i<T.length();i++){
            if(T.charAt(i)!=35){
                T_RES = T_RES + T.charAt(i);
            }
            if(T.charAt(i)==35 && !T_RES.equals("")){
                T_RES = T_RES.substring(0,T_RES.length() - 1);
            }
        }

        if(S_RES.equals(T_RES)){
            System.out.print(true);
        }else {
            System.out.print(false);
        }


    }
}
