class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def isBalanced(root):
    def helper(root):
        if not root:
            return [True, 0]
        left, right = helper(root.left), helper(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])]
    return helper(root)[0]

"""
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def check(root):
        if root is None:
            return 0
        left, right = check(root.left), check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
        
    return check(root) != -1
"""

"""
def isBalanced_helper(root):
    if root is None:
        return 0
    leftheight = isBalanced_helper(root.left)
    if left == -1:
        return -1
    rightheight = isBalanced_helper(root.right)
    if right == -1:
        return -1
    if abs(leftheight - rightheight) > 1:
        return -1
    return max(leftheight, rightheight)

def isBalanced(root):
    return isBalanced_helper(root) > -1
"""