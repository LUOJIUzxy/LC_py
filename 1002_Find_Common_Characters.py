from ast import List


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
        