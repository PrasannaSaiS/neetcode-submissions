from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))

            mp[sorted_str].append(s)
        return list(mp.values())