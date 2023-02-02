/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {

    dummy := &ListNode{Next: head}
    cur := head
    prev := dummy
    keep := &ListNode{Next: nil}
    for cur != nil && cur.Next != nil {
        keep = cur.Next.Next
        cur.Next.Next = cur
        prev.Next = cur.Next
        cur.Next = keep

        prev = cur
        cur = cur.Next
    }

    return dummy.Next
}