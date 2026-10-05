class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
                if s[i - 1] == '(':
                    score += 1 << count
        return score