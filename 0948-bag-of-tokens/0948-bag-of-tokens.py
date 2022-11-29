class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens:
            return 0
        if power < tokens[0]:
            return 0
        i ,j = 0, len(tokens)-1
        score = 0
        answer = 0
        while j >= i:
            print(power)
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                answer = max(answer, score)
            elif power < tokens[j]:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                return answer
        
        return answer
                
            
            