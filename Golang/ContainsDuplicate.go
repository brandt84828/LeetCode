func containsDuplicate(nums []int) bool {

    m := make(map[int]bool, len(nums))

    for _, value := range nums {
        if _, ok:=m[value]; ok {
            return true
        } else {
            m[value] = true
        }
    }

    return false
    
}