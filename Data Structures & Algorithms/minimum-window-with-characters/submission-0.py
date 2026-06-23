class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        # Count character requirements for string t
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1

        # 'missing' tracks total characters needed to make a valid window
        missing = len(t)
        l = start = 0
        min_len = float("inf")

        for r in range(len(s)):
            # If s[r] is a desired character, decrement the total missing count
            if counts.get(s[r], 0) > 0:
                missing -= 1
            
            # Decrease the count required for this character (can go negative)
            counts[s[r]] = counts.get(s[r], 0) - 1

            # When the window is valid, try to shrink it from the left
            while missing == 0:
                # Update the minimal window dimensions
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start = l

                # Slide the left pointer out of the window
                counts[s[l]] += 1
                # If this character was critical to t, we now miss it
                if counts[s[l]] > 0:
                    missing += 1
                
                l += 1

        return s[start : start + min_len] if min_len != float("inf") else ""