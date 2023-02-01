func removeDuplicates(nums []int) int {
    
    insert := 1
    for i:=1;i < len(nums);i++ {
        if nums[i] != nums[i-1] {
            nums[insert] = nums[i]
            insert = insert + 1
        }
    }
    return insert
}