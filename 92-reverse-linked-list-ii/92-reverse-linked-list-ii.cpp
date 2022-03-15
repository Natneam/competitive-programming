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
    ListNode* reverse(ListNode* node, int length){
        ListNode* prev = NULL;
        ListNode* curr = node;
        ListNode* temp = NULL;
        
        for(int i = 0; i < length; i++){
            
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        
        ListNode* ans = prev;
        
        while(prev->next != NULL){
            prev = prev->next;
        }
        prev->next = curr;
        return ans;
    }
    
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* prev = NULL;
        ListNode* dummy_node = new ListNode();
        ListNode* curr = dummy_node;
        
        curr->next = head;
        int length = right - left;
        
        if (length == 0){
            return head;
        }
        
        
        for(int i = 0; i < left ; i++){
            prev = curr;
            curr = curr->next;
        }
        
        prev->next = reverse(curr, length + 1);
        
        return dummy_node->next;
    }
};