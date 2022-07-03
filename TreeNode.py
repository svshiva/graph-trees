class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        
        if(val): self.val = val
        if (left):
            if isinstance(left, TreeNode):self.left = left
            else: raise TypeError
        else: self.left=None
        if (right):
            if isinstance(right, TreeNode):self.right = right
            else: raise TypeError
        else: self.right=None
    
