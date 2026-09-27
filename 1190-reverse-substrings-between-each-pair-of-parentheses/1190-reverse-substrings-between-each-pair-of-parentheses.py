class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = [0] * n
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                open_idx = stack.pop()
                pair[open_idx] = i
                pair[i] = open_idx
        ans = []
        step = 1
        i = 0
        while 0 <= i < n:
            if s[i].islower():
                ans.append(s[i])
            else:
                i = pair[i]
                step = -step
            i += step
        return ''.join(ans)