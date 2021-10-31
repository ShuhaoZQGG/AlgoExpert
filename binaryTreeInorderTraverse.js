/**
 * Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:

    Input: root = [1,null,2,3]
    Output: [1,3,2]
    Example 2:

    Input: root = []
    Output: []
    Example 3:

    Input: root = [1]
    Output: [1]
    Example 4:


    Input: root = [1,2]
    Output: [2,1]
    Example 5:


    Input: root = [1,null,2]
    Output: [1,2]

 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

// Recursive Solution
const inorderTraversal = function(root) {
  let result = [];
  dfs(root);

  const dfs = function(root) {
    if (root){
      root = root.left;
      result.push(root.val)
      root = root.right;
    }
  }

  return result;
}

// Interative Soluition

const inorderTraversal = function(root) {
    let result = [];
    let stack = [];
    while(true) {
      if (root) {
        stack.push(root)
        root = root.left
      } else {
        if(stack.length === 0) break;
        root = stack.pop();
        result.push(root.val);
        root = root.right;
      }
    }

    return result;
};

console.log(inorderTraversal([1,null,2,3]));