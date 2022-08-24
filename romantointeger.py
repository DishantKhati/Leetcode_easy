class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        subs = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        if len(maps) <= 0 or not s:
            return 0    
        cal, char = 0, ""
        for i in range(len(s)):
            if char + s[i] in subs:
                cal -= maps[char]
                cal += subs[char + s[i]]
                char = s[i]
            else:
                cal += maps[s[i]]
                char = s[i]
        return cal
