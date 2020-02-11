/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if(root == NULL || root == p || root == q)
        return root;
    struct TreeNode * left, *right;
    left = lowestCommonAncestor(root->left, p,q);
    right = lowestCommonAncestor(root->right, p,q);
    if(!left && !right)
        return NULL;
    else if(left&& right == NULL)
        return left;
    else if(left == NULL && right != NULL)
        return right;
    else
        return root;
}