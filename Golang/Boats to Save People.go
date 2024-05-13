#1
func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    start := 0
    end := len(people) - 1
    res := 0
    for start <= end {
       if people[start] + people[end] <= limit {
           start++
           end--
           res++
       } else {
           end--
           res++
       }
    }
    return res
}

#2
func numRescueBoats(people []int, limit int) int {
    sort.Slice(people, func(i, j int) bool {
        return people[i] > people[j]
    })
    start := 0
    end := len(people) - 1
    for start <= end {
       if people[start] + people[end] <= limit {
           end--
       }
       start++
    }
    return start
}