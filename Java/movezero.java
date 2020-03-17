public class movezero {
    public void moveZeroes(int[] nums) {
        int zero = 0;
        int temp;
        for(int i=1;i<nums.length;i++){

            if(nums[zero]!=0){

                zero = zero + 1;
            }

            temp = nums[zero];
            nums[zero] = nums[i];
            nums[i] = temp;

        }

        System.out.print(nums);

    }
}
