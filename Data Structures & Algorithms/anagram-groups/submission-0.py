class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in hm:
                hm[sorted_string].append(s)
            else:
                hm[sorted_string] = [s]

        
        result = []

        for key in hm:
            result.append(hm[key])

        return result