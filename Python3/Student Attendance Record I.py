#1
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for c in s:
            if c == 'A':
                absent+=1
                if absent >= 2:
                    return False
            if c == 'L':
                late+=1
                if late >= 3:
                    return False
            else:
                late = 0
        
        return True
            
#2
class Solution:
    def checkRecord(self, s: str) -> bool:
        return (s.count('A') < 2) and ('LLL' not in s)
            