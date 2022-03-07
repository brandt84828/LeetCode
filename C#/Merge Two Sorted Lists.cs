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
public class Solution21 {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode head = new ListNode(0);
        ListNode dummy = head;
        
        while(list1!=null&&list2!=null)
        {
            if(list1.val<=list2.val)
            {
                head.next = list1;
                list1 = list1.next;
            }
            else
            {
                head.next = list2;
                list2 = list2.next;
            }
            head = head.next;
        }
        
        head.next = list1 ?? list2;
        
        return dummy.next;
        
    }
}