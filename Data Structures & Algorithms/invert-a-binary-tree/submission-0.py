# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level wise trvalsal 
        # append induviuval level in revers order 
        if root == None:
            return None
        dq = deque()
        dq.append(root)

        while(dq):
            n=len(dq)

            while(n):
                node=dq.pop()
                node.left,node.right=node.right,node.left
                if node.left is not None:
                    dq.append(node.left)

                if node.right is not None:
                    dq.append(node.right)
                
                n-=1
        
        return root
            


        