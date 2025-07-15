class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(magazine) < len(ransomNote)):
            return False

        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False

        return True