class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # .sort() returns num but sorts it.
        # must do sorted(s) which sorts s in-place
        return sorted(s) == sorted(t)