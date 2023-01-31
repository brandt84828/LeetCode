/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummyNode := &ListNode{}
    cur := dummyNode

    for list1 != nil && list2 != nil {
        if list1.Val > list2.Val {
            cur.Next = list2
            list2 = list2.Next
        } else {
            cur.Next = list1
            list1 = list1.Next
        }
        cur = cur.Next
    }

    if list1 != nil {
        cur.Next = list1
    } else if list2 != nil{
        cur.Next = list2
    }

    return dummyNode.Next
}