# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def dfs(node):
            no = TreeNode(node)
            for child, dirx in graph[node]:
                if dirx:
                    no.left = dfs(child)
                else:
                    no.right = dfs(child)
            return no

        alls = set()
        chis = set()
        graph = defaultdict(list)
        for node in descriptions:
            par, chi, l = node
            alls.add(par)
            alls.add(chi)
            chis.add(chi)
            graph[par].append((chi, l))
        
        root = (alls - chis).pop()
        return dfs(root)