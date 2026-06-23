class Solution:
    def checkInclusion(self, s1, s2):
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if len(s1) > len(s2):
            return False
            
        # Create character frequency arrays for s1 and the current window in s2
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate the initial frequencies for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # If the first window matches, we found a permutation immediately
        if s1_count == s2_count:
            return True
            
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Check if the frequencies match
            if s1_count == s2_count:
                return True
                
        return False