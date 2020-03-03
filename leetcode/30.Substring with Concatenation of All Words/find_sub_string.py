class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "":
            return []
        total = 0
        the_map = {}
        for word in words:
            total += 1
            if the_map.has_key(word):
                the_map[word] = the_map[word] + 1
            else:
                the_map[word] = 1
        rs = []
        if total == 0:
            return []
        word_len = len(words[0])
        if len(s) < total * word_len:
            return []
        for i in range(0, len(s) - word_len * total+1):
            temp_map = {}
            for j in range(0, total):
                key = s[i+j* word_len :i + (j+1) * word_len]
                if temp_map.has_key(key):
                    temp_map[key] += 1
                else:
                    temp_map[key] = 1
            if cmp(the_map, temp_map) == 0:
                rs.append(i)
        return rs


if __name__ == '__main__':
    print Solution().findSubstring( "wordgoodgoodgoodbestword", ["word","good","best","good"])

