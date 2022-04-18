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
    void traverse(TreeNode* node, vector<int>& elements){
        if(!node) return;
        traverse(node->left, elements);
        elements.push_back(node->val);
        traverse(node->right, elements);
    }
    
    int kthSmallest(TreeNode* root, int k) {
        
        vector<int> elements{};
        traverse(root, elements);
        return elements[k-1];
    }
};