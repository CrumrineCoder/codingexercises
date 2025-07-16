from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfiedChildren = 0

        while len(g) > 0 and len(s) > 0:
            child = g[0]
            cookie = s[0]
            if (child <= cookie):
                satisfiedChildren += 1
                del g[0]
                del s[0]
            else:
                del s[0]
        return satisfiedChildren

sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1]))