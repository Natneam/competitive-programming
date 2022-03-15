/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int val = 0;
        ListNode* ans = new ListNode();
        
        ListNode* curr_node = ans;
        
        while(l1 != NULL || l2 != NULL){
            if(l1 != NULL && l2 != NULL){
                val = l1->val + l2->val + carry;
                l1 = l1->next;
                l2 = l2->next;
            } else if (l1 != NULL){
                val = l1->val + carry;
                l1 = l1->next;
            } else {
                val = l2->val + carry;
                l2 = l2->next;
            }
            
            carry = val / 10;
            val = val % 10;
             
            curr_node->next = new ListNode(val);
            
            curr_node = curr_node->next;
        }
        
        if(carry != 0){
            curr_node -> next = new ListNode(carry);
        }
        
        return ans->next;        
    }
};