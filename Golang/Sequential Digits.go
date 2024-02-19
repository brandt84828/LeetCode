func sequentialDigits(low int, high int) []int {
    queue := []int{1, 2, 3, 4, 5, 6, 7 ,8 ,9}
    var res []int
    for len(queue) > 0 {
        elem := queue[0]
        queue = queue[1:]
        if low <= elem && elem <=high {
            res = append(res, elem)
        }
        last := elem % 10
        if last < 9 {
            queue = append(queue, elem*10 + last + 1)
        }
    }
    return res
}