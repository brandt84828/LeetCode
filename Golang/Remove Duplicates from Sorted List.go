//1
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    curr := head

    if head == nil || head.Next == nil {
        return head
    }

    for curr.Next != nil {
        if curr.Val == curr.Next.Val {
            curr.Next = curr.Next.Next
        } else {
            curr = curr.Next
        }
    }

    return head
}

//2
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    cur := head
    for cur != nil {
        if cur.Next != nil && cur.Val == cur.Next.Val {
            cur.Next = cur.Next.Next
            continue
        }
        cur = cur.Next
    }
    
    return head
}