class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0]*n
        stk = []
        for item in logs:
            item_list = item.split(':')
            if item_list[1]=='start':
                item_list.append(0)
                stk.append(item_list)
            if item_list[1]=='end':
                start = stk.pop()
                duration = int(item_list[2])-int(start[2])+1
                exclusive = duration-start[3]
                idx = int(start[0])
                answer[idx]+=exclusive
                if len(stk)!=0:
                    stk[-1][3]+= duration
        return answer
                