#1
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        sa = [c for c in s]
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while l < r:
            if sa[l] in vowels:
                if sa[r] in vowels:
                    sa[l], sa[r] = sa[r], sa[l]
                    r = r - 1
                    l = l + 1
                else:
                    r = r - 1
            else:
                l = l + 1
        
        return ''.join(sa)

#2
class Solution(object):
    def reverseVowels(self, s):
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        # Loop until the start pointer is no longer less than the end pointer.
        while start < end:
            # Move the start pointer towards the end until it points to a vowel.
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Move the end pointer towards the start until it points to a vowel.
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Swap the vowels found at the start and end positions.
            word[start], word[end] = word[end], word[start]
            
            # Move the pointers towards each other for the next iteration.
            start += 1
            end -= 1
        
        # Convert the character array back to a string and return the result.
        return "".join(word)

#3
class Solution(object):
    def reverseVowels(self, s):
        #(?i) makes it match case insensitive and
        # hello > ['e', 'o']
        vowels = re.findall('(?i)[aeiou]', s)
        
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)