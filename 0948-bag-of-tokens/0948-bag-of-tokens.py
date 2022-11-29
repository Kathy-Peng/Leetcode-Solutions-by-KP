class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens:
            return 0
        if power < tokens[0]:
            return 0
        i ,j = 0, len(tokens)-1
        score = 0
        max_score = 0
        while j >= i:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                if score > max_score:
                    max_score = score
            elif power < tokens[j]:
                power += tokens[j]
                score -= 1
                j -= 1
        return max_score
                
            
            