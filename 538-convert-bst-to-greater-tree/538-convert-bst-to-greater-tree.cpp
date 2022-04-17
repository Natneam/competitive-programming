/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int postOrderUpdate(TreeNode* node, int currVal){
        if(!node) return 0;
        
        if(node->right) currVal = postOrderUpdate(node->right, currVal);
        currVal = currVal + node->val;
        node->val = currVal;
        if (node->left) currVal = postOrderUpdate(node->left, node->val);
        
        return currVal;
    }
    
    TreeNode* convertBST(TreeNode* root) {
        postOrderUpdate(root, 0);
        return root;
    }
};