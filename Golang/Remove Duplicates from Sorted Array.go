func removeDuplicates(nums []int) int {
    count := 1
    for i :=1; i < len(nums);i ++{
        if nums[i] > nums[count-1] {            
            nums[count] = nums[i]
            count = count + 1
        }
    }
    return count
}


func removeDuplicates(nums []int) int {
    j := 1
    for i:=1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            nums[j] = nums[i]
            j++
        }
    }
    return j
}

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