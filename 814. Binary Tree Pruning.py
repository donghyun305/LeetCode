from idlelib.tree import TreeNode
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = TreeNode()

        if not root:
            return None
        if self.pruneTree(root.left) == None :
            root.left = None
        if self.pruneTree(root.right) == None:
            root.right = None
        if root.val == 0 and root.left==None and root.right==None:
            root = None
        return root
