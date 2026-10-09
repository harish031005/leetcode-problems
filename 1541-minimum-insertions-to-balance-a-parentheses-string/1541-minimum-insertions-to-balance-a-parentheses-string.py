class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        need = 0
        ans = 0
        for c in s:
            if c == '(':
                if need % 2:
                    ans += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    ans += 1
                    need = 1
        return ans + need