class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        dic = Counter(hand)
        while dic:
            min_value = min(dic.keys())
            for j in range(groupSize):
                if min_value in dic:
                    dic[min_value] -= 1
                    if dic[min_value] == 0:
                        del dic[min_value]
                    min_value += 1
                else:
                    return False
        return True
                
                
        