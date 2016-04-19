class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        a = 0
        lst = []
        while a < len(s):
            if s[a] not in lst:
                lst.append(s[a])
                result = len(lst) if len(lst) > result else result
            else:
                lst = lst[lst.index(s[a]) + 1:]
 
                lst.append(s[a])
 
                result = len(lst) if len(lst) > result else result
            a += 1
        return result




