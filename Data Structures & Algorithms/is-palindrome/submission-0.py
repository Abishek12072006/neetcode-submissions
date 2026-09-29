class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for ch in s.lower():
            if ch.isalnum():
                a=a+ch
        if a==a[::-1]:
            return True
        return False
