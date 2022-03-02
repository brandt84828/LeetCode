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
public class Solution2 {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        
        var r = new ListNode(-1);
        var n = r;
        int carry = 0;
        
        while(carry > 0 || l1!=null || l2!=null)
        {
            var sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
            carry = (int)(sum / 10);
            
            n.next = new ListNode(sum % 10);
            n = n.next;
            l1 = l1?.next;
            l2 = l2?.next;
        }
        
        return r.next;
    }
}