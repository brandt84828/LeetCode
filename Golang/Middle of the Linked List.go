//1
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    
    slow, fast := head, head

    for(  fast != nil && fast.Next != nil ) {
        fast = fast.Next.Next
        slow = slow.Next
    }
    return slow
}

//2
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    
    count := 0
    curr := head

    for curr != nil {
        curr = curr.Next
        count++
    }

    count = count / 2
    

    for count > 0 {
        head = head.Next
        count--
    }

    return head
}