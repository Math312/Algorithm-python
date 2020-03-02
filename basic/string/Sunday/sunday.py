class Solution(object):
    def findStr(self, str, sub):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        def find_char(sub_str, char):
            char_index = -1
            for i in range(0, len(sub_str)):
                if sub_str[i] == char:
                    char_index = i
            return char_index
        if str == sub or sub == "":
            return 0
        i = 0
        j = 0
        while i <= len(str)-len(sub):
            if str[i+j] == sub[j]:
                j += 1
                if j == len(sub):
                    return i
            else:
                temp = i + len(sub)
                if temp >= len(str):
                    break
                index = find_char(sub,str[temp])
                if index == -1:
                    i += len(sub)
                else:
                    j = 0
                    i = i + len(sub) - index
        return -1


