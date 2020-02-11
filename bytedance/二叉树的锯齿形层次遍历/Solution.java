/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList();
        if(root == null){
            return result;
        }
        List<Integer> list = new ArrayList();
        Stack<TreeNode> stack = new Stack();
        Stack<TreeNode> temp = new Stack();
        stack.push(root);
        Boolean fromLeft = true;
        int size = 1;
        while(!stack.empty()){
            TreeNode node = stack.pop();
            list.add(node.val);
            if(fromLeft){
                if(node.left != null){
                    temp.push(node.left);
                }
                if(node.right != null){
                    temp.push(node.right);
                }
            }else{
                if(node.right != null){
                    temp.push(node.right);
                }
                if(node.left != null){
                    temp.push(node.left);
                }
            }
            size --;
            if(size == 0){
                result.add(new ArrayList<>(list));
                list.clear();
                stack = temp;
                size = stack.size();
                temp = new Stack();
                fromLeft = !fromLeft;
            }
        }
        
        return result;
    }
}