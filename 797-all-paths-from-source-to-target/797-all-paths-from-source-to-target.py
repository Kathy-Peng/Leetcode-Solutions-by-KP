class Solution(object):
    def helper(self, graph, stack, partial_result, results):
            while len(stack)!=0:
                curr = stack.pop()
                if curr==len(graph)-1:
                    partial_copy = partial_result[:]
                    partial_copy.append(curr)
                    results.append(partial_copy)
                else:
                    for child in graph[curr]:
                        partial_copy = partial_result[:]
                        partial_copy.append(curr)
                        self.helper(graph,[child], partial_copy, results)

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        results = []
        stack = graph[0]
        self.helper(graph, stack, [0], results)
        return results