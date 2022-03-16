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
    vector<TreeNode*> generatesubTrees(int start, int end){
        
        vector<TreeNode*> ans;
        vector<TreeNode*> right_subtrees;
        vector<TreeNode*> left_subtrees;
        
        TreeNode* node;
        
        if (start == end) return vector<TreeNode*>{new TreeNode(start)};
        
        for(int i = start; i <= end; i++){
            if (i != start){
                left_subtrees = generatesubTrees(start, i-1);
            } else {
                left_subtrees = {NULL};
            }
            
            if (i != end){
                right_subtrees = generatesubTrees(i+1, end);
            } else {
                right_subtrees = {NULL};
            }
            
            for(int j = 0; j < right_subtrees.size(); j++){
                for(int k = 0; k < left_subtrees.size(); k++){
                    node = new TreeNode(i, left_subtrees[k], right_subtrees[j]);
                    ans.push_back(node);
                }
            }
        }
        return ans;
    }
    
    vector<TreeNode*> generateTrees(int n) {
        return generatesubTrees(1, n);
    }
};