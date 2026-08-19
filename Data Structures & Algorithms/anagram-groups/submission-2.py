class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for words in strs:
            key = "".join(sorted(words))
            if key in d:
                d[key].append(words)
            else:
                d[key]=[words]

        return list(d.values())                
        