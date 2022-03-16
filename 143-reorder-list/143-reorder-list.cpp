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
    void reorderList(ListNode* head) {
        ListNode* curr_node = head;
        int length = 0;
        
        if(head->next == NULL || head->next->next == NULL){
            return;
        }
        
        // finding the length
        while(curr_node){
            curr_node = curr_node->next;
            length += 1;
        }
        
        stack<ListNode*> stk;
        curr_node = head;
        
        for(int i=1; i < length / 2; i++){
            curr_node = curr_node->next;
        }
        
        ListNode* temp = curr_node->next;
        curr_node->next = NULL;
        curr_node = temp;
        
        while(curr_node){
            temp = curr_node->next;
            curr_node->next = NULL;
            stk.push(curr_node);
            curr_node = temp;
        }
        
        while(!stk.empty()){
            temp = head->next;
            head->next = stk.top();
            head->next->next = temp;
            stk.pop();
            
            if(head->next->next != NULL)
                head = head->next->next;
            else head = head->next;
        }
    }
};