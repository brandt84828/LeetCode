/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution24 {
    public ListNode SwapPairs(ListNode head) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        
        while(curr.next!=null && curr.next.next!=null)
        {
            ListNode swap1 = curr.next;
            ListNode swap2 = curr.next.next;
            
            swap1.next = swap2.next;
            swap2.next = swap1;
            curr.next = swap2;
            
            curr = swap1;
        }
        
        return dummy.next;
    }
}