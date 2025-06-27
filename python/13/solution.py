class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        result = 0
        while (i < len(s)):
            current_val = roman_map[s[i]]

            if (i+1 < len(s)):
                next_val = roman_map[s[i+1]]
                if(current_val < next_val):
                    result += next_val-current_val
                    i+=2
                else:
                    result += current_val
                    i+=1
            
            else:
                result += current_val
                i+=1 
        return result                