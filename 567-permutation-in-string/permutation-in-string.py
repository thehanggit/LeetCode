class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)
        for char in s1:
            s1_map[char] += 1
        
        s2_map = defaultdict(int)
        for char in s2[0:len(s1)]:
            s2_map[char] += 1
        
        if s1_map == s2_map:
            return True
        
        for i in range(len(s1),len(s2)):
            s2_map[s2[i]] += 1
            left_char = s2[i - len(s1)]
            
            s2_map[left_char] -= 1
            if s2_map[left_char] == 0:
                del s2_map[left_char]

            if s1_map == s2_map:
                return True

        return False 