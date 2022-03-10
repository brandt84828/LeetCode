public class Solution121 {
    public int MaxProfit(int[] prices) {
        int lsf = Int32.MaxValue;
        int op = 0;
        int pist = 0;
        
        for(int i = 0; i < prices.Length; i++){
            if(prices[i] < lsf){
                lsf = prices[i];
            }
            pist = prices[i] - lsf;
            if(op < pist){
                op = pist;
            }
        }
        return op;
    }
}