# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        判断 B 树是否为 A 中的子结构
        """
        def doesTree1HasTree2(tree1: TreeNode, tree2: TreeNode ) -> bool:
            """
            判断 Tree2 是否为 Tree1 中包含根结点的子结构
            """
            if tree2 is None: return True
            if tree1 is None: return False
            if tree1.val != tree2.val: return False
            return doesTree1HasTree2(tree1.left, tree2.left) and doesTree1HasTree2(tree1.right, tree2.right)
        
        result = False
        if A is not None and B is not None:
            if A.val == B.val:
                result = doesTree1HasTree2(A, B)
            if result is False:
                result = self.isSubStructure(A.left, B)
            if result is False:
                result = self.isSubStructure(A.right, B)
        return result
        


