class Leaderboard:

    def __init__(self):
        self.hash = {}
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.hash:
            self.hash[playerId]+= score
        else:
            self.hash[playerId] = score
        
    def top(self, K: int) -> int:
        score_list = []
        for player, score in self.hash.items():
            score_list.append(score)
        score_list = sorted(score_list)
        des_score_list = score_list[::-1]
        total_score = des_score_list[:K]
        return sum(total_score)

    def reset(self, playerId: int) -> None:
        self.hash[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)