//1
package main

import (
	"sort"
	"strconv"
)

type MyInt struct {
	Val int
	Index int
}

func findRelativeRanks(nums []int) []string {
	athletes := make([]MyInt, len(nums))
	for i, num := range nums {
		athletes[i].Index=i
		athletes[i].Val=num
	}
	sort.Slice(athletes, func(i, j int) bool {
		return athletes[i].Val>athletes[j].Val
	})
	rank := make([]string, len(nums))
	for i, athlete := range athletes {
		switch i {
		case 0:
			rank[athlete.Index]="Gold Medal"
		case 1:
			rank[athlete.Index]="Silver Medal"
		case 2:
			rank[athlete.Index]="Bronze Medal"
		default:
			rank[athlete.Index] = strconv.Itoa(i+1)
		}
	}
	return rank

}

//2
func findRelativeRanks(score []int) []string {
    var temp []int
    mp := map[int]int{}
    var ans []string

    temp = append(temp, score...)

    sort.Sort(sort.Reverse(sort.IntSlice(temp)))
    for i := range temp{
        mp[temp[i]] = i+1
    }
    
    for i := range score{
        if mp[score[i]] == 1{
            ans = append(ans, "Gold Medal")
        }else if mp[score[i]] == 2 {
            ans = append(ans, "Silver Medal")
        }else if mp[score[i]] == 3{
            ans = append(ans,  "Bronze Medal")
        }else{
            num := strconv.Itoa(mp[score[i]])
            ans = append(ans, num)
        }
    }

    return ans
}