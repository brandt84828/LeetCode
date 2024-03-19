#1
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fre = {}
        maxFre = 1

        for n in nums:
            if n in fre:
                fre[n] += 1
                if fre[n] > maxFre:
                    maxFre = fre[n]
            else:
                fre[n] = 1
        res = 0
        for k, v in fre.items():
            if v == maxFre:
                res = res + v

        return res
        

#2
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
        
        max_frequency = max(freq_counter.values())
        
        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
        
        total_frequency = max_frequency * len(max_freq_elements)
        
        return total_frequency
        

#3
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        di=defaultdict(int)
        m,c=0,0
        for i in nums:
            di[i]+=1
            if di[i]>m:
                m=di[i]
                c=0
            if di[i]==m:
                c+=1
        return m*c
        