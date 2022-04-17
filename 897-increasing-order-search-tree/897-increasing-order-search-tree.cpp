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
    void helper(TreeNode* node, vector<int>& values){
        if(!node) return;
        helper(node->left, values);
        values.push_back(node->val);
        helper(node->right, values);
    }
    
    TreeNode* increasingBST(TreeNode* root) {
        //pre order traversal
        vector<int> values{};
        helper(root, values);
        TreeNode* inOrderTree{new TreeNode(0)};
        TreeNode* currNode{inOrderTree};
        for(auto n : values){
            currNode->right = new TreeNode(n);
            currNode = currNode->right;
        }
        
        return inOrderTree->right;
    }
};