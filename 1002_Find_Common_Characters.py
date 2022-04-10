from ast import List
from collections import defaultdict
from collections import Counter
#used three loops so the time complexity is pretty high
#Considered the common letters should be in all strings, so I traverse all letters in the first word(words[0]) and compare them with other letters in the following words
#if one matches, then record its index and sum up all the indexes recorded to see if it matches the sum from 1 to len(words) - 1, which equals len(words)*(len(words-1)/2
#if it does, then means every word has the mutual letter, so add it to the result list
#But need to take care that the matched letter should be removed out of the corresponding word, in case that it would be counted as another duplicate mutual letter in the following matches(which in fact only one exists)
#['book', 'rock', 'goose'] 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #define the initial list_a as all the seperate letters in words[0]
        list_a = []
        q = 0
        #print(len(words))
        #print(len(words)*(len(words) - 1)/2)
        for q in range(len(words[0])):
            i = 1
            i_sum = 0
            for i in range(1, len(words)):
                j = 0
                for j in range(len(words[i])):
                    if words[0][q] == words[i][j]:
                        print('letter' + words[0][q])
                        i_sum += i
                        print(i_sum)
                        words[i] = words[i][:j] + words[i][j + 1:]
                        print(words[i])
                        break
            if i_sum == len(words)*(len(words) - 1)/2:         
                list_a.append(words[0][q])
                print(list_a)
        
        return list_a

#first optimization
#64ms
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # build a filter based on the first word
        w = words[0]
        d = Counter(w)
        
        for s in words[1:]:
            ds = Counter(s)
            del_list = []
            for k in d.keys():
                if not k in ds.keys():
                    del_list.append(k)
            
            for dl in del_list:
                del d[dl]
            # 1. remove all the difference (d.keys - d intersect ds)            
            #for dl in del_list:
             #   del d[dl]
            for k, v in ds.items():
                if k in d.keys():
                    d[k] = min(d[k], ds[k])
           
            # 2. update the existing letter's frequency
            #for k, v in ds.items():
             #   if k in d.keys() and ds[k] <= d[k]:
              #      d[k] = ds[k]
        
        ans = []
        # populate ans from the original filter
        for k, v in d.items():
            #to output the repeated letters
            for i in range(v):
                ans.append(k)
        return ans

#second optimization
#56ms
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count(word):
            res = defaultdict(lambda: 0)
            for c in word:
                res[c] = res[c] + 1
            return res
        
        def minCount(c1, c2):
            res = defaultdict(lambda: 0)
            for c in c1.keys():
                res[c] = min(c1[c],c2[c])
            return res
        
        res = count(words[0])
        for word in words[1:]:
            res = minCount(count(word),res)

        chars = []
        for c in res.keys():
            chars = chars + [c]*res[c]
        return chars
        