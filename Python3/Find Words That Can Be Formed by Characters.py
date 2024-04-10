#1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum += len(word)
        return sum

#2 all == > [true,true,true] = true, [true,false,true] = false
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, ct = 0, collections.Counter
        chars_counter = ct(chars)
        for word in words:
            word_counter = ct(word)
            if all(word_counter[c] <= chars_counter[c] for c in word_counter):
                sum += len(word)
        return sum