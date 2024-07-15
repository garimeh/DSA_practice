# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = set()
        par_chi = defaultdict(list)
        for node in descriptions:
            par, no, l = node
            parent = TreeNode(par)
            parents.add(par)
            children.add(no)
            par_chi[par].append((no, l))
        
        root = TreeNode(list(parents.difference(children))[0])
        q = deque([root])

        while q:
            parent = q.popleft()
            for chval, l, in par_chi[parent.val]:
                child = TreeNode(chval)
                q.append(child)
                if l:
                    parent.left = child
                else:
                    parent.right = child
        return root