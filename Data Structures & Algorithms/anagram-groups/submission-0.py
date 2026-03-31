class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = []
            dic[sorted_word].append(word)
        
        if len(dic) == 0:
            return [[""]]

        res = []

        for value in dic.values():
            res.append(value)

        return res