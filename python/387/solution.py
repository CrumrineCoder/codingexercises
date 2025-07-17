class Solution:
    def firstUniqChar(self, s: str) -> int:
        candidates = {}
        for i in range(0, len(s)):
            if s[i] not in candidates:
                candidates[s[i]] = i
            elif candidates[s[i]] != -1:
                candidates[s[i]] = -1

        for value in candidates.values():
            if value != -1:
                return value
        return -1
sol = Solution()
print(sol.firstUniqChar("leetcode"))