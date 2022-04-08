from ast import List

def lastStoneWeight(self, stones: List[int]):
        #y is the heaviest, x is the second heaviest
    
        while len(stones) >= 0:
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            else:
                y = stones[0] 
                y_index = 0
                for index in range(len(stones)):
                    if y < stones[index]:
                        y = stones[index]
                        y_index = index
                    else:
                        continue
                #del stones[y_index]
                
                if y_index == 0:
                    x = stones[1]
                    x_index = 1
                if y_index != 0:
                    x = stones[0] 
                    x_index = 0
                for index in range(len(stones)):
                    if x < stones[index] and index != y_index:
                        x = stones[index]
                        x_index = index

                if x == y:
                    del stones[x_index]
                    del stones[y_index]

                if x != y:
                    stones[y_index] = y - x
                    del stones[x_index]