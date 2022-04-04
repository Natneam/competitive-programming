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
    ListNode* swapNodes(ListNode* head, int k) {
        
        ListNode* frontNode = head;
        int frontCounter{1};

        while(frontCounter < k){
            frontCounter++;
            frontNode = frontNode->next;
        }
        
        ListNode* backNode = frontNode;
        ListNode* tempHead = head;
        
        while(backNode->next){
            backNode = backNode->next;
            tempHead = tempHead->next;
        }
        
        int temp = frontNode->val;
        frontNode->val = tempHead->val;
        tempHead->val = temp;
    
        return head;
        
    }
    
};