class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        players = set()
        answer_0 = []
        answer_1 = []
        for match in matches:
            winner, loser = match
            if winner not in players:
                players.add(winner)
            if loser not in players:
                players.add(loser)
            hashmap[loser] += 1
        
        for player in players:
            if player not in hashmap.keys():
                answer_0.append(player)
            elif hashmap[player] == 1:
                answer_1.append(player)
        answer_0.sort()
        answer_1.sort()
        
        return [answer_0, answer_1]