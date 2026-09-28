class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        ans = 0
        for c in s:
            if c == '(':
                depth += 1
                ans = max(ans, depth)
            elif c == ')':
                depth -= 1
        return ans