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
    


def validate(root:TreeNode)->bool:
    if(root.left==None and root.right==None): return True

    if (root.left != None and root.right != None):
        if not(root.val>=root.left.val and root.val<=root.right.val):
            return False
        return validate(root.left) and validate(root.right)
    elif root.left!=None:
        if root.val<root.left.val:
            return False
        return validate(root.left) 
    elif root.right!=None:
        if root.val>root.right.val:
            return False
        return validate(root.right) 

def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    

    print(validate(root)) 


if __name__=='__main__': main()

    
   
