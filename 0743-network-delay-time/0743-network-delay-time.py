from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #step 1: create adjacency matrix from times
        adj_max = {}
        for item in times:
            if item[0] in adj_max:
                curr = adj_max[item[0]]
                curr.append([item[1], item[2]])
                adj_max[item[0]]=curr
            else:
                adj_max[item[0]]=[[item[1], item[2]]]
        #step 2: initialize the priority queue and visited_set
        pq = PriorityQueue()
        pq.put((0, k))
        visited = set()
        visited.add(k)
        while not pq.empty():
            prev_cost, node = pq.get()
            visited.add(node)
            #step 3: add node to visited once it's been popped from the pq
            #and terminate search once all the nodes are visited
            if len(visited)==n:
                return prev_cost
            if node not in adj_max:
                continue
            for item in adj_max[node]:
                neighbor = item[0]
                curr_cost = item[1]
                total_cost = prev_cost + curr_cost
                #step 4: calculate the total cost by adding current cost and prev_cost(cost of parent node)
                if neighbor not in visited:
                    pq.put((total_cost, neighbor))
        return -1
                    
                    
                
                
            
            
            
        
        
        