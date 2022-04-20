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
class BSTIterator {
public:
    vector<TreeNode*> stk{};
    TreeNode* curr;
    
    BSTIterator(TreeNode* root) {
        curr = root;
        
        while(curr){
            stk.push_back(curr);
            curr = curr->left;
        }
    }
    
    int next() {
        int ans = stk.back()->val;
        curr = stk.back() -> right;
        stk.pop_back();
        
        while(curr){
            stk.push_back(curr);
            curr = curr->left;
        }

        return ans;
    }
    
    bool hasNext() {
        return stk.size() != 0;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */