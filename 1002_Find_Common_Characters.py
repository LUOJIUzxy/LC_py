from ast import List
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
        print(len(words))
        print(len(words)*(len(words) - 1)/2)
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
        