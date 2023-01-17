/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    dummy := new(ListNode)
    curr := dummy
    carry := 0

    for l1 != nil || l2 != nil || carry > 0 {
        if l1 != nil {
            carry = carry + l1.Val
            l1 = l1.Next
        }

        if l2 != nil {
            carry = carry + l2.Val
            l2 = l2.Next
        }
        
        curr.Next = &ListNode{carry % 10, nil}
        carry = carry / 10
        curr = curr.Next
    }

    return dummy.Next
    
}