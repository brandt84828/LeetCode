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
public class Solution83 {
    public ListNode DeleteDuplicates(ListNode head) {
        
        if(head == null || head.next == null)
            return head;
        
        ListNode list = head;
        
        while(list.next!=null)
        {
            if(list.val==list.next.val)
            {
                list.next = list.next.next;
            }
            else
            {
                list = list.next;
            }
        }
        
        return head;
    }
}