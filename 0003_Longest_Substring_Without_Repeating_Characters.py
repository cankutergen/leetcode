class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest
