class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize bad_count and character_count for string t
        character_count = defaultdict(int)
        bad_count = 0
        for c in t: 
            bad_count += 1
            character_count[c] -= 1

        best_l, best_r = -int(1e9), -1
        
        l = 0
        for r in range(len(s)):
            if character_count[s[r]] < 0:
                bad_count -= 1
            character_count[s[r]] += 1

            # Adjust the left pointer to shrink the window
            while bad_count == 0 and character_count[s[l]] > 0:
                character_count[s[l]] -= 1
                l += 1

            # Update best_l and best_r for the smallest window
            if bad_count == 0 and best_r - best_l > r - l:
                best_l, best_r = l, r

        if best_l == -1:
            return ""
        return s[best_l:best_r+1]
