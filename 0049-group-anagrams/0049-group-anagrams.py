class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts=defaultdict(list)
        for str in strs:
            key="".join(sorted(str))
            dicts[key].append(str)
        return list(dicts.values())    