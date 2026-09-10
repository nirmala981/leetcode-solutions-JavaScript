class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maximum):
            if node is None:
                return 0

            count = 0

            if node.val >= maximum:
                count = 1

            maximum = max(maximum, node.val)

            count += dfs(node.left, maximum)
            count += dfs(node.right, maximum)

            return count

        return dfs(root, root.val)
        