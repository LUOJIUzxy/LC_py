from ast import List
#find the heaviest stone at first and record its index ->y, y_index
#then find the second heaviest stone by setting it larger than other stones but smaller or equal than y and record its index -> x, x_index
#but if the y_index is 0, in order to let x to be different from y, should set x starting from index 1
#Also, remember to change the value of y first and delete x_index afterwards, cause delete action would affect index

#46ms
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

#1. possible optimization: find the heaviest stone  ---->  use the sort() method in python to directly get the first two heaviest stones
#50ms
def lastStoneWeight(self, stones: List[int]):
        #y is the heaviest, x is the second heaviest
    
        while len(stones) >= 0:
            stones.sort()
            
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            
            y = stones[-1]
            x = stones[-2]
            
            #if x == y:
            stones.pop()
            stones.pop()
            
            if x != y:         
                stones.append(y - x)