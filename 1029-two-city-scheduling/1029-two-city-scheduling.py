class Solution(object):
    def argsort(self, diffs):
        return sorted(range(len(diffs)),key=diffs.__getitem__)
    
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #to know who should fly to city B we calculate the cost incurred if we fly each person to city B instead of city A
        #the n people who incur the least cost of flying to city B instead of A will be flied to city B
        #step 1: calculate the diff for each person and map each diff element to person
        diffs = []
    
        for i in range(len(costs)):
            item = costs[i]
            diff = item[1]-item[0]
            diffs.append(diff)
        #step 2: sort the diff array in ascending order
        diffs_idx = self.argsort(diffs)
        #step 3: first n person goes to B calculate the cost of flying to B
        total_cost = 0
        for j in range(len(costs)//2):
            person = diffs_idx[j]
            total_cost += costs[person][1]
        #step 4: add the cost of flying to A to get total cost 
        for k in range(len(costs)//2, len(costs)):
            person = diffs_idx[k]
            total_cost += costs[person][0]
        return total_cost