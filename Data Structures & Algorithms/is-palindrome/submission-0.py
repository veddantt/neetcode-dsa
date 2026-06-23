class Solution(object):
    def isPalindrome(self, s):
        rev_str = ''
        for i in s:
            if i.isalnum():
                rev_str += i.lower()
        return rev_str == rev_str[::-1]