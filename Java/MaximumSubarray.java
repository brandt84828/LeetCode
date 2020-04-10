public class MaximumSubarray {
    public static void main(String[] args) {
        int nums[] = {-2,1,-3,4,-1,2,1,-5,4};
        int sum = nums[0];
        int ans = nums[0];

        for(int i=1;i<nums.length;i++){
            sum = Math.max(sum+nums[i],nums[i]);//累加比對，然後下面逐一比對更新最大值，跑完陣列即得ans
            if(sum>ans){
                ans = sum;
            }
        }
        System.out.print(ans);


    }
}
