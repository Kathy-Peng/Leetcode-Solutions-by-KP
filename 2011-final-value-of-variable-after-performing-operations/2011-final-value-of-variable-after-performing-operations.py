class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hashmap = {'++X':1, 'X++':1, '--X':-1, 'X--':-1}
        output = 0
        for item in operations:
            output += hashmap[item]
        return output