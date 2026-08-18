class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= []
        for a in s:
            if a.isalnum():
                l.append(a.lower())
        return l == l[::-1]