class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        knowledge_map = {key: value for key, value in knowledge}
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                closing = s.find(')', i + 1)
                key = s[i + 1:closing]
                result.append(knowledge_map.get(key, '?'))
                i = closing + 1
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)