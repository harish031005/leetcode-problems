class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0
        close_count = 0
        ans = 0
        for c in s:
            if c == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                ans = max(ans, 2 * close_count)
            if close_count > open_count:
                open_count = close_count = 0
        open_count = close_count = 0
        for c in reversed(s):
            if c == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                ans = max(ans, 2 * open_count)
            if open_count > close_count:
                open_count = close_count = 0
        return ans