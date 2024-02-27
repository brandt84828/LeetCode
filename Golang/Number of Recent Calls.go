type RecentCounter struct {
    q []int
}


func Constructor() RecentCounter {
    return RecentCounter{[]int{}}
}


func (this *RecentCounter) Ping(t int) int {
    this.q = append(this.q, t)
    for i, val := range this.q {
        if val >= t - 3000 {
            this.q = this.q[i:]
            break
        }
    }
    return len(this.q)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */